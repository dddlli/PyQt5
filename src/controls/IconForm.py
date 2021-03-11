import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class IconForm(QMainWindow):
    def __init__(self,parent=None):
        super(IconForm,self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,250)
        #设置主窗口的标题
        self.setWindowTitle('设置桌面图标')
        #设置窗口的尺寸
        self.setWindowIcon(QIcon('./images/c5.ico'))
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/c1.ico'))
    main = IconForm()
    main.show()

    sys.exit(app.exec_())