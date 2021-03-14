from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        layout = QHBoxLayout()

        self.button1 = QRadioButton('The First QRadioButton')
        self.button1.setChecked(True)

        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('The Second QRadioButton')
        self.button1.setChecked(False)

        self.button2.toggled.connect(self.buttonState)

        layout.addWidget(self.button2)
        self.resize(400,300)
        self.setLayout(layout)
    def buttonState(self):
        radioButton = self.sender()
        if radioButton.text() == 'The First QRadioButton':
            if radioButton.isChecked() == True:
                print('<' + radioButton.text() + '>被选中')
            else:
                print('<' + radioButton.text() + '被取消选中状态')
        if radioButton.text() == 'The Second QRadioButton':
            if radioButton.isChecked() == True:
                print('<' + radioButton.text() + '>被选中')
            else:
                print('<' + radioButton.text() + '被取消选中状态')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/c6.ico'))
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())