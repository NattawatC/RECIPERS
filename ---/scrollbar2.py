import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class scrollbar2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrollbar")
        self.setGeometry(100, 100, 500, 500)
        self.create_scrollbar()
    
    def create_scrollbar(self):
        self.vbox = QVBoxLayout()
        self.scroll = QScrollArea()
        self.buf = QWidget()
        self.vbox2 = QVBoxLayout()
        
        for i in range(1,50):
            object = QLabel("TextLabel")
            self.vbox2.addWidget(object)
        self.buf.setLayout(self.vbox2)
         
            
        
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.buf)
        self.vbox.addWidget(self.scroll)
        
        self.setLayout(self.vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = scrollbar2()
    window.show()
    sys.exit(app.exec())  