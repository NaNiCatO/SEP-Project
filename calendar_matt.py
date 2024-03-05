import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.calendar = QCalendarWidget(self)
        self.setCentralWidget(self.calendar)

        # Dates to highlight
        highlight_dates = [4, 7, 12, 18,19,20,21,22]
        for day in highlight_dates:
            month = self.calendar.monthShown()
            year = self.calendar.yearShown()
            date = QDate(year, month, day)
            self.calendar.setDateTextFormat(date, self.highlight_format())

    def highlight_format(self):
        text_format = self.calendar.dateTextFormat(QDate())
        text_format.setForeground(Qt.red)  # You can set any color you want here
        text_format.setBackground(Qt.yellow)  # You can set any color you want here
        return text_format


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())