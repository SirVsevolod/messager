from PyQt5 import QtWidgets
import clientui
import requests

class MessengerWindow(QtWidgets.QMainWindow,clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.sendMessege)

    def sendMessege(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        text = self.textEdit.toPlainText()
        print(username,password,text)

        if not username:
            self.addText("ERROR:username is empty!")
        if not password:
            self.addText("ERROR:password is empty!")
        if not text:
            self.addText("ERROR:text is empty!")

        r = requests.post("http://127.0.0.1:5000/send",
    					json = {"username":username,"password":password,"text":text}
                        )
        if not r.json()["ok"]:
            print("ERROR:Access denied!")

        self.textEdit.clear()

    def addText(self,text):
        self.textBrowser.append(text)

app = QtWidgets.QApplication([])
window = MessengerWindow()
window.show()
app.exec_()
