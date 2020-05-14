#!/usr/bin/python
from PyQt5 import QtWidgets ,QtCore
import clientui
import requests
from datetime import *

class MessengerWindow(QtWidgets.QMainWindow,clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.sendMessege)
        self.last_message_time = 0
        self.timer  = QtCore.QTimer()
        self.timer.timeout.connect(self.getUpdates)
        self.timer.start(1000)

    def sendMessege(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.textEdit.toPlainText()
       

        if not username:
            self.addText("ERROR:username is empty!")
            self.addText(" ")
            return
        if not password:
            self.addText("ERROR:password is empty!")
            self.addText(" ")
            return
        if not text:
            self.addText("ERROR:text is empty!")
            self.addText(" ")
            return

        r = requests.post("http://127.0.0.1:5000/send",
    					json = {"username":username,"password":password,"text":text}
                        )
        if not r.json()["ok"]:
            self.addText("ERROR:Access denied!")
            self.addText(" ")
            return

        self.textEdit.clear()
        self.textEdit.repaint()


    def addText(self,text):
        self.textBrowser.append(text)
        self.textEdit.repaint()


    def getUpdates(self):
        r = requests.get("http://127.0.0.1:5000/history",
        params = {'after':self. last_message_time})
    
        data = r.json()
        for  massage in data['messages']:

            beauty_time = datetime.fromtimestamp(massage['time'])
            beauty_time = beauty_time.strftime("%H:%M:%S")

            self.addText(beauty_time + " " + massage['username'])
            self.addText(massage['text'])
            self.addText(" ")
            self.last_message_time = massage["time"]


app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec_()
