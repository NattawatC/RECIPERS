from PySide6.QtCore import Qt, QMimeData, QPoint
from PySide6.QtGui import QDrag, QMouseEvent, QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class DraggableWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(100, 50)
        self.setStyleSheet("background-color: red;")

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.startDrag()

    def startDrag(self):
        self.hide()  # Hide the widget before starting the drag operation

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setData("application/x-widget", b"")
        drag.setMimeData(mime_data)

        # Set a pixmap representation of the widget for dragging
        pixmap = self.grab()
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        self.render(painter, QPoint(), self.rect())
        painter.end()
        drag.setPixmap(pixmap)

        result = drag.exec_(Qt.MoveAction)
        if result == Qt.IgnoreAction:  # Widget was dragged out of the program
            self.deleteLater()  # Delete the widget


if __name__ == "__main__":
    app = QApplication([])

    # Create the main window
    main_window = QWidget()
    main_window.setWindowTitle("Draggable Widget")
    main_window.resize(500, 500)

    # Create a layout for the main window
    layout = QVBoxLayout(main_window)
    layout.setAlignment(Qt.AlignTop)

    # Create a draggable widget
    widget = DraggableWidget(main_window)
    layout.addWidget(widget)

    main_window.show()
    app.exec()
