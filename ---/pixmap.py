import sys
import requests
from PySide6.QtGui     import QPixmap, QScreen
from PySide6.QtWidgets import QApplication, QWidget, QLabel

URL = 'https://bojongourmet.com/wp-content/uploads/2018/07/Green-Goddess-Potato-Salad-13.jpg#'


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('getAndSetImageFromURL()')
        self.label = QLabel(self)
        self.pixmap = QPixmap()
        self.getAndSetImageFromURL(URL)
        self.resize(self.pixmap.width(), self.pixmap.height())
        screenSize = QScreen.availableGeometry(QApplication.primaryScreen())
        frmX = (screenSize.width() - self.width()) / 2
        frmY = (screenSize.height() - self.height()) / 2
        self.move(frmX, frmY)
        self.show()

    def getAndSetImageFromURL(self, imageURL):
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        self.label.setPixmap(self.pixmap)
        # QApplication.processEvents() # uncoment if executed on loop


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = App()
    sys.exit(app.exec())
