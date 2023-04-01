import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Scrollbar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrollbar")
        
        self.create_scrollbar()
        
    def create_scrollbar(self):
        self.scroll = QScrollArea()             
        self.widget = QWidget()                
        self.vbox = QVBoxLayout()          

        for i in range(1,50):
            object = QLabel("TextLabel")
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Scroll Area Demonstration')
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scrollbar()
    window.show()
    sys.exit(app.exec())         