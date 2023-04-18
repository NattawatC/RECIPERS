import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Scrollbar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrollbar")


        self.scroll = QScrollArea()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Scrollbar()
    window.show()
    sys.exit(app.exec())         