import os
from PySide6.QtGui import QFont


class Theme:
    __ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    __THEME_PATH = os.path.join(__ROOT_DIR, "theme.qss")

    # Font
    CHILLAX_REGULAR_14 = QFont("Chillax")
    CHILLAX_REGULAR_14.setPixelSize(14)

    CHILLAX_REGULAR_16 = QFont("Chillax")
    CHILLAX_REGULAR_16.setPixelSize(16)

    CHILLAX_REGULAR_20 = QFont("Chillax")
    CHILLAX_REGULAR_20.setPixelSize(20)

    CHILLAX_REGULAR_24 = QFont("Chillax")
    CHILLAX_REGULAR_24.setPixelSize(24)

    CHILLAX_REGULAR_36 = QFont("Chillax")
    CHILLAX_REGULAR_36.setPixelSize(36)
    
    CHILLAX_REGULAR_40 = QFont("Chillax")
    CHILLAX_REGULAR_40.setPixelSize(40)

    CHILLAX_BOLD_20 = QFont("Chillax")
    CHILLAX_BOLD_20.setPixelSize(20)
    CHILLAX_BOLD_20.setBold(True)

    CHILLAX_BOLD_36 = QFont("Chillax")
    CHILLAX_BOLD_36.setPixelSize(36)
    CHILLAX_BOLD_36.setBold(True)

    CHILLAX_SEMI_BOLD_32 = QFont("Chillax")
    CHILLAX_SEMI_BOLD_32.setPixelSize(32)
    CHILLAX_SEMI_BOLD_32.setBold(True)

    CHILLAX_BOLD_40 = QFont("Chillax")
    CHILLAX_BOLD_40.setPixelSize(40)
    CHILLAX_BOLD_40.setBold(True)

    CHILLAX_BOLD_65 = QFont("Chillax")
    CHILLAX_BOLD_65.setPixelSize(65)
    CHILLAX_BOLD_65.setBold(True)

    CHILLAX_BOLD_80 = QFont("Chillax")
    CHILLAX_BOLD_80.setPixelSize(80)
    CHILLAX_BOLD_80.setBold(True)

    CHILLAX_BOLD_70 = QFont("Chillax")
    CHILLAX_BOLD_70.setPixelSize(70)
    CHILLAX_BOLD_70.setBold(True)


    @staticmethod
    def get_stylesheet() -> str:
        """get style from theme.qss file"""
        stylesheet: str
        with open(Theme.__THEME_PATH, "r") as file:
            stylesheet = file.read()
        file.close()
        return stylesheet

    #Colors (Just in case)
    # DARK_BROWN = "4A321C"
    # LIGHT_BROWN = "754926"
    # CREAM = "D8B797"
    # EGG_WHITE = "F9F5F0"