import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QRect, QCoreApplication
from PySide6.QtGui import QPixmap, QFont, Qt, QCursor


class ScrollAreaExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scroll Area Example')
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout(self)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        content_layout = QVBoxLayout(scroll_content)
        for i in range(20):
            label = QLabel(f'This is label {i}')
            content_layout.addWidget(label)

        scroll_area.setGeometry(50, 50, 300, 200)  # Set the geometry of scroll_area

        layout.addWidget(scroll_area)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScrollAreaExample()
    sys.exit(app.exec())