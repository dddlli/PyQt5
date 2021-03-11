import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QPushButton,QApplication,QWidget
from PyQt5.QtGui import QIcon

def onClick_button():
    print("1")
    print("widget.x() = %d" % widget.x())
    print("widget.y() = %d" % widget.y())
    print("widget.width() = %d" % widget.width())
    print("widget.height() = %d" % widget.height())

    print("2")
    print("widget.geometry().x() = %d" % widget.geometry().x())
    print("widget.geometry().y() = %d" % widget.geometry().y())
    print("widget.geometry().width() = %d" % widget.geometry().width())
    print("widget.geometry().height() = %d" % widget.geometry().height())

    print("3")
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x())
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y())
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width())
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height())
app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("button")
btn.clicked.connect(onClick_button)

btn.move(24,52)

widget.resize(300,240)
widget.move(250,200)
widget.setWindowTitle('屏幕坐标系')
widget.show()
app.setWindowIcon(QIcon('./images/c3.ico'))
sys.exit(app.exec_())