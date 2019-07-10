from PyQt5 import QtCore, QtGui, QtWidgets
import time
import sys, os

class Ui_frmClient(object):
    def __init__(self, frmClientTerminal):

        self.setupUi(frmClientTerminal)
        self.retranslateUi(frmClientTerminal)
        self.button_clicked()
        
    def setupUi(self, frmClientTerminal):
        frmClientTerminal.setObjectName("frmClientTerminal")
        frmClientTerminal.resize(823, 464)
        self.centralwidget = QtWidgets.QWidget(frmClientTerminal)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 641, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lblListOfConnection = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblListOfConnection.setFont(font)
        self.lblListOfConnection.setObjectName("lblListOfConnection")
        self.horizontalLayout_11.addWidget(self.lblListOfConnection)
        spacerItem = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.lblDetails = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        self.lblDetails.setFont(font)
        self.lblDetails.setObjectName("lblDetails")
        self.horizontalLayout_11.addWidget(self.lblDetails)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 265, 721, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(570, 290, 241, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.btnStartClient = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(22)
        self.btnStartClient.setFont(font)
        self.btnStartClient.setAutoFillBackground(False)
        self.btnStartClient.setObjectName("btnStartClient")
        self.verticalLayout_9.addWidget(self.btnStartClient)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lblInputIP = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblInputIP.setObjectName("lblInputIP")
        self.horizontalLayout_12.addWidget(self.lblInputIP)
        spacerItem1 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.linInputIP = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.linInputIP.setObjectName("linInputIP")
        self.horizontalLayout_12.addWidget(self.linInputIP)
        self.verticalLayout_10.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.lblPort = QtWidgets.QLabel(self.layoutWidget_2)
        self.lblPort.setObjectName("lblPort")
        self.horizontalLayout_13.addWidget(self.lblPort)
        spacerItem2 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.linPort = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.linPort.setObjectName("linPort")
        self.horizontalLayout_13.addWidget(self.linPort)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.txtDetails = QtWidgets.QTextEdit(self.centralwidget)
        self.txtDetails.setGeometry(QtCore.QRect(570, 30, 241, 231))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        self.txtDetails.setFont(font)
        self.txtDetails.setReadOnly(True)
        self.txtDetails.setObjectName("txtDetails")
        self.lblStatusLog = QtWidgets.QLabel(self.centralwidget)
        self.lblStatusLog.setGeometry(QtCore.QRect(10, 265, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lblStatusLog.setFont(font)
        self.lblStatusLog.setObjectName("lblStatusLog")
        self.txtStatusUpdate = QtWidgets.QTextEdit(self.centralwidget)
        self.txtStatusUpdate.setGeometry(QtCore.QRect(10, 290, 541, 131))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(10)
        self.txtStatusUpdate.setFont(font)
        self.txtStatusUpdate.setReadOnly(True)
        self.txtStatusUpdate.setObjectName("txtStatusUpdate")
        self.lstTransferredFiles = QtWidgets.QListWidget(self.centralwidget)
        self.lstTransferredFiles.setGeometry(QtCore.QRect(12, 32, 541, 231))
        self.lstTransferredFiles.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.lstTransferredFiles.setObjectName("lstTransferredFiles")
        frmClientTerminal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmClientTerminal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName("menubar")
        frmClientTerminal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmClientTerminal)
        self.statusbar.setObjectName("statusbar")
        frmClientTerminal.setStatusBar(self.statusbar)

        self.retranslateUi(frmClientTerminal)
        QtCore.QMetaObject.connectSlotsByName(frmClientTerminal)

    def retranslateUi(self, frmClientTerminal):
        _translate = QtCore.QCoreApplication.translate
        frmClientTerminal.setWindowTitle(_translate("frmClientTerminal", "Client Terminal"))
        self.lblListOfConnection.setText(_translate("frmClientTerminal", "Transferred Files"))
        self.lblDetails.setText(_translate("frmClientTerminal", "Item Details"))
        self.btnStartClient.setText(_translate("frmClientTerminal", "START"))
        self.lblInputIP.setText(_translate("frmClientTerminal", "IP Address"))
        self.linInputIP.setText(_translate("frmClientTerminal", "192.168.1.97"))
        self.lblPort.setText(_translate("frmClientTerminal", "Port Number"))
        self.linPort.setText(_translate("frmClientTerminal", "8000"))
        self.lblStatusLog.setText(_translate("frmClientTerminal", "Status Log:"))

    def button_clicked(self):
        self.btnStartClient.clicked.connect(self.set_client_for_ui)
    
    def set_client_for_ui(self):
        global client
        self.txtStatusUpdate.append('Initializing client...')
        try:
            input_ip = self.linInputIP.text()
            input_port = int(self.linPort.text())
        except ValueError:
            self.txtStatusUpdate.append('Error: Bad Input')
            return
        client = sw.Client()
        if client.set_client_connection(input_ip, input_port, 5):
            self.txtStatusUpdate.append('Error: Failed to start client')
        self.txtStatusUpdate.append('Connected to server')
        self.btnStartClient.setDisabled(True)
        self.btnStartClient.setText('Connected')
            
    


if __name__ == "__main__":
    sys.path.append(os.getcwd())
    import lib.socket_wrapper as sw
    client = None



    app = QtWidgets.QApplication(sys.argv)
    ClientTerminal = QtWidgets.QMainWindow()
    ui = Ui_frmClient(ClientTerminal)

    ClientTerminal.show()
    sys.exit(app.exec_())

