import sys
import MainWinMenuToolsBar

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinMenuToolsBar.Ui_MainWindow()
    #向主窗口
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())