import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10 
        self.top = 10
        self.width = 200
        self.height =100 
        self.count = 0
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QLabel('Count = {}    '.format(self.count),self)
        self.label.move(30,55)
        button = QPushButton('Increment', self)
        button.setToolTip('Click button to increment count.')
        button.move(30,30) 
        button.clicked.connect(self.on_click)
 
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        self.count = self.count + 1
        #print('Count = {}'.format(self.count))
        self.label.setText("Count = {}    ".format(self.count))
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
