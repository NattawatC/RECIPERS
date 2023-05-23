import sys
from PySide6.QtWidgets import *


class ScrollAreaExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scroll Area Example')
        self.setGeometry(300, 300, 400, 300)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        layout = QVBoxLayout(scroll_content)
        for i in range(20):
            label = QLabel(f'This is label {i}')
            layout.addWidget(label)

        self.setCentralWidget(scroll_area)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScrollAreaExample()
    sys.exit(app.exec_())