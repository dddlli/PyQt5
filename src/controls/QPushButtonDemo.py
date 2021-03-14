from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QPushButtonDemo(QWidget):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()
        self.button1 = QPushButton('The first button')
        self.button1.setText('First Button1')
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))
        layout.addWidget(self.button1)

        self.button2 = QPushButton('Image Button')
        self.button2.setIcon(QIcon(QPixmap('./images/c2.ico')))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('Unvaliable Button')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&My Button')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda :self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(400,300)

    def buttonState(self):
        if self.button1.isChecked():
            print('Press')
        else:
            print('No Press')

    def whichButton(self,btn):
        print('Which is the Pressed button<' + btn.text() + '>')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/c6.ico'))
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())