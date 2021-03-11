import sys
from PyQt5.QtWidgets import QApplication,QHBoxLayout,QWidget,QMainWindow,QPushButton
from PyQt5.QtGui import QIcon

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        #t添加Button
        self.button1 = QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)
    #按钮单击的方法（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        #退出应用程序
        app.quit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/c2.ico'))
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())