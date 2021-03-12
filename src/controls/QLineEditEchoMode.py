'''
QLineEditEchoMode
基本功能：（输入单行文本）
EchoMode（回显模式）

1.Normal
2.Noecho
3.Password
4.PasswordEchoOnEdit
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEdit = QLineEdit()

        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("Noecho",noEchoLineEdit)
        formLayout.addRow("Password",passwordLineEdit)
        formLayout.addRow("passwordEchoOnEdit",passwordEchoOnEdit)

        #placeholdertext
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("Echo")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEdit.setPlaceholderText("passwordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/c6.ico'))
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())