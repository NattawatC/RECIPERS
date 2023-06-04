from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


def isHTML(text):
    if text == "":
        return True
    try:
        print(text)
        parser = etree.HTMLParser()
        etree.HTML(text, parser)
        print(etree.HTML(text, parser))
        return True
    except Exception:
        return False