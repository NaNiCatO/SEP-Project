from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *



class ClickableTaskFrame(QFrame):
    clicked = Signal(object)

    def __init__(self, task, *args, **kwargs):
        super(ClickableTaskFrame, self).__init__(*args, **kwargs)
        self.task = task

    def mousePressEvent(self, event):
        self.clicked.emit(self.task)

    def enterEvent(self, event):
        self.setStyleSheet("background-color: lightgray;")  # Change background color to light gray on hover

    def leaveEvent(self, event):
        self.setStyleSheet("background-color: white;")  # Revert back to white background when not hovered
