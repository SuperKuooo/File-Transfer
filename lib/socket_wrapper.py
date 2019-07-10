import socket
import os
import time
import shutil
import datetime
from watchdog.observers import Observer as OBS

DATE = datetime.date.today()
DATE_TIME = datetime.datetime.now()
DEFAULT_IP = '192.168.1.118'
DEFAULT_PORT = 8000
BUFFER_SIZE = 4096


def zip_folder(output, target):
    print("Zipping Target...")
    try:
        shutil.make_archive(output, "zip", target)
    except shutil.Error:
        print("Error: Failed to zip file")

def check_connection(list_of_connection):
    _list = []
    i = 0
    for _socket in list_of_connection:
        temp = Client(_socket)
        temp.send_string('0')
        if temp.recv(1) == 1:
            _list.append(list_of_connection[i])
            list_of_connection.pop(i)
        i += 1
    return _list


class Client:
    def __init__(self, conn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
        self.s = conn
        self.name = socket.gethostname()

    def set_client_connection(self, TCP_IP, TCP_PORT, attempt_to_reconnect=0):
        try:
            self.s.settimeout(2)
            self.s.connect((TCP_IP, TCP_PORT))
        except socket.error:
            print("Error: Failed to connect to server")
            if attempt_to_reconnect:
                print("Retrying in " + str(attempt_to_reconnect) + " seconds...")
                time.sleep(attempt_to_reconnect)
                print("Starting client...")
                self.set_client_connection(TCP_IP, TCP_PORT, attempt_to_reconnect)
            return 1
        return 0

    def get_client_name(self):
        return self.name

    def confirm_connection(self, message=None):
        if not message:
            message = self.name + '///is online'
        self.s.settimeout(5)
        data = self.s.recv(BUFFER_SIZE)
        if data.decode("utf-8") != message:
            raise UserWarning('Error: different echo value')
        print('Echo Success')
        return 0

    def recv(self, buffer_size):
        try:
            self.s.settimeout(3600)
            return self.s.recv(buffer_size)
        except socket.error:
            print('Warning: Timeout')
            return None
        except KeyboardInterrupt:
            return 'break'

    def send_string(self, message, raw=False):
        b = message
        if not raw:
            b = bytes(message, 'utf-8')
        try:
            self.s.send(b)
        except socket.error:
            print('Error: Failed to send message')
            return 1
        return 0

    def send_image(self, location):
        try:
            with open(location, 'rb') as fp:
                b = bytearray(fp.read())
                self.s.sendall(b)
        except socket.error:
            print("Error: Failed to send image")
            return 1
        return 0

    def send_zip(self, location):
        try:
            with open(location, 'rb') as fp:
                self.s.sendall(fp.read())
                print("Sending")
        except socket.error:
            print("Error: Failed to send zip")
            return 1
        return 0

    def save_file(self, buffer, filepointer):
        print('zip received')
        while True:
            data = self.s.recv(buffer)
            if not data:
                break
            filepointer.write(data)
        print('zip saved')

    def close(self):
        self.send_string('terminating')
        self.s.close()


class Server:
    def __init__(self):
        self.list_of_connection = []
        self.list_of_observer = []
        self.name = socket.gethostname()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def set_server_connection(self, TCP_IP=DEFAULT_IP, TCP_PORT=DEFAULT_PORT, attempt_to_reconnect=0):
        try:
            self.s.bind((TCP_IP, TCP_PORT))
        except socket.error:
            print("Error: Failed to start server")
            if attempt_to_reconnect:
                print("Retrying in " + str(attempt_to_reconnect) + " seconds...")
                time.sleep(attempt_to_reconnect)
                self.set_server_connection(
                    TCP_IP, TCP_PORT, attempt_to_reconnect)
            return 1
        return TCP_IP, TCP_PORT

    def set_list_of_connection(self, _socket, operation=0, index=None):
        if operation == 0:
            # Append
            self.list_of_connection.append(_socket)
        elif operation == 1:
            # Set new list
            self.list_of_connection = _socket
        elif operation == 2:
            # Delete item by index
            if index != None:
                self.list_of_connection.pop(index)
        elif operation == 3:
            self.list_of_connection.clear()
        else:
            print('Error: Invalid operation')

    def set_list_of_observer(self, _observer, operation=0, index=None):
        if operation == 0:
            self.list_of_observer.append(_observer)
        elif operation == 2:
            if index != None:
                self.list_of_observer.pop(index)
        

    def get_num_of_connection(self):
        return len(self.list_of_connection)

    def get_num_of_observer(self):
        return len(self.list_of_observer)

    def get_list_of_connection(self, index=None):
        if index == None:
            return self.list_of_connection
        else:
            return self.list_of_connection[None]

    def get_server_name(self):
        return self.name

    def echo_connection(self, conn, message):
        message = message.decode("utf-8")
        try:
            temp = Client(conn)
            temp.send_string(message)
            self.set_list_of_connection(conn)
        except socket.error:
            print("Error: Failed to echo client connection")

        return 0

    def broadcast_string(self, message, client_index=None):
        if client_index == None:
            target_audience = self.get_list_of_connection()
        else:
            target_audience = self.get_list_of_connection(client_index)

        for conn in target_audience:
            try:
                temp = Client(conn)
                temp.send_string(message)
                print('Sending zip')
            except socket.error:
                print("Error: Failed to send message")
                return 1
        return 0

    def broadcast_zip(self, location, client_index=None):
        if client_index == None:
            target_audience = self.get_list_of_connection()
        else:
            target_audience = self.get_list_of_connection(client_index)

        for conn in target_audience:
            try:
                with open(location, 'rb') as fp:
                    conn.sendall(fp.read())
            except socket.error:
                print("Error: Failed to send zip")
                return 1
        return 0

    def close(self):
        for conn in self.list_of_connection:
            conn.close()
        for obs in self.list_of_observer:
            obs.close()
        return self.s.close()

    def listen(self, size):
        return self.s.listen(size)

    def accept(self):
        return self.s.accept()


class Observer:
    def __init__(self, server, lib_path, target_path):
        self.obs = OBS()
        self.server = server
        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)
        self.handler = Handler(server, lib_path, target_path)

    def set_server(self, server):
        self.server = server

    def get_target_path(self):
        return self.target_path

    def start_observe(self, recursive=False):
        self.obs.schedule(self.handler, self.tot_path, recursive)
        self.obs.start()

    def close(self):
        self.obs.stop()
        self.obs.join()


class Handler:
    def __init__(self, server, lib_path, target_path):
        self.server = server
        self.lib_path = lib_path
        self.target_path = target_path
        self.tot_path = os.path.join(lib_path, target_path)

    def dispatch(self, event):
        if(event.src_path.endswith('.log')):
            print('Logfile Modified')
            filename = os.path.join('./archive', self.target_path, str(DATE))
            zip_folder(filename, self.tot_path)
            self.server.broadcast_string('zip')
            time.sleep(0.1)
            self.server.broadcast_zip(os.path.join('./archive', self.target_path, str(DATE) + '.zip'))
            print('done shipping')