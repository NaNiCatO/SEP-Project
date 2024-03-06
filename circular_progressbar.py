import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow, QLabel, QFrame
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QColor, QFont, QLinearGradient, QPainterPath, QBrush, QPen
from ui_py.main_stack import Ui_MainWindow
from class_module import Task_handlers

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(4)

        # Add CircularProgressBarExample widget to right_content_detail1
        circular_progress_widget_1 = CircularProgressBarExample(96)
        self.container1 = QVBoxLayout(self.ui.frame_26)
        self.container1.addWidget(circular_progress_widget_1)

        # Add CircularProgressBarExample widget to frame_28
        circular_progress_widget_2 = CircularProgressBarExample(52)
        self.container2 = QVBoxLayout(self.ui.frame_28)
        self.container2.addWidget(circular_progress_widget_2)


        circular_progress_widget_3 = CircularProgressBarExample(45)
        self.container3 = QVBoxLayout(self.ui.normal_task_anal)
        self.container3.addWidget(circular_progress_widget_3)


        circular_progress_widget_4 = CircularProgressBarExample(1)
        self.container4 = QVBoxLayout(self.ui.urgent_task_anal)
        self.container4.addWidget(circular_progress_widget_4)


        # Start timer to update the progress bars
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(60)  # Update progress every 20 milliseconds

    def update_progress(self):
        circular_progress_widget_1 = self.ui.frame_26.findChild(CircularProgressBarExample)
        if circular_progress_widget_1 is not None:
            circular_progress_widget_1.update_progress()

        circular_progress_widget_2 = self.ui.frame_28.findChild(CircularProgressBarExample)
        if circular_progress_widget_2 is not None:
            circular_progress_widget_2.update_progress()


class Analysis_page(QMainWindow):
    def __init__(self, ui : Ui_MainWindow, tasks : Task_handlers):
        super().__init__()
        self.ui = ui
        self.tasks = tasks
        self.number_of_tasks = self.tasks.number_of_tasks()
        self.percentage_Normal_task = int((self.tasks.number_of_upcoming_tasks() + self.tasks.number_of_today_tasks()) / self.number_of_tasks * 100)
        self.percentage_Urgent_task = int(self.tasks.number_of_urgent_tasks() / self.number_of_tasks * 100)
        self.percentage_Delayed_task = int(self.tasks.number_of_late_tasks() / self.number_of_tasks * 100)
        self.percentage_Completed_task = int(self.tasks.number_of_completed_tasks() / self.number_of_tasks * 100)
        self.Remaining_task = self.number_of_tasks - self.tasks.number_of_completed_tasks()
        font = QFont()
        font.setPointSize(38)
        font.setBold(True)
        self.ui.label_6.setText(f"{self.Remaining_task}")
        self.ui.label_6.setStyleSheet("color: #008080;")
        self.ui.label_6.setFont(font)

        # Add CircularProgressBarExample widget to right_content_detail1
        circular_progress_widget_1 = CircularProgressBarExample(self.percentage_Completed_task)
        self.container1 = QVBoxLayout(self.ui.frame_26)
        self.container1.addWidget(circular_progress_widget_1)

        # Add CircularProgressBarExample widget to frame_28
        circular_progress_widget_2 = CircularProgressBarExample(self.percentage_Delayed_task)
        self.container2 = QVBoxLayout(self.ui.frame_28)
        self.container2.addWidget(circular_progress_widget_2)


        circular_progress_widget_3 = CircularProgressBarExample(self.percentage_Urgent_task)
        self.container3 = QVBoxLayout(self.ui.normal_task_anal)
        self.container3.addWidget(circular_progress_widget_3)


        circular_progress_widget_4 = CircularProgressBarExample(self.percentage_Normal_task)
        self.container4 = QVBoxLayout(self.ui.urgent_task_anal)
        self.container4.addWidget(circular_progress_widget_4)


        # Start timer to update the progress bars
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(60)  # Update progress every 20 milliseconds

    def update_progress(self):
        circular_progress_widget_1 = self.ui.frame_26.findChild(CircularProgressBarExample)
        if circular_progress_widget_1 is not None:
            circular_progress_widget_1.update_progress()

        circular_progress_widget_2 = self.ui.frame_28.findChild(CircularProgressBarExample)
        if circular_progress_widget_2 is not None:
            circular_progress_widget_2.update_progress()

    def update_ui(self):
        self.number_of_tasks = self.tasks.number_of_tasks()
        self.percentage_Normal_task = int((self.tasks.number_of_upcoming_tasks() + self.tasks.number_of_today_tasks()) / self.number_of_tasks * 100)
        self.percentage_Urgent_task = int(self.tasks.number_of_urgent_tasks() / self.number_of_tasks * 100)
        self.percentage_Delayed_task = int(self.tasks.number_of_late_tasks() / self.number_of_tasks * 100)
        self.percentage_Completed_task = int(self.tasks.number_of_completed_tasks() / self.number_of_tasks * 100)
        self.Remaining_task = self.number_of_tasks - self.tasks.number_of_completed_tasks()
        font = QFont()
        font.setPointSize(38)
        font.setBold(True)
        self.ui.label_6.setText(f"{self.Remaining_task}")
        self.ui.label_6.setStyleSheet("color: #008080;")
        self.ui.label_6.setFont(font)

        #clear everything in container layout
        while self.container1.count():
            item = self.container1.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        while self.container2.count():
            item = self.container2.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        while self.container3.count():
            item = self.container3.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        while self.container4.count():
            item = self.container4.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        circular_progress_widget_1 = CircularProgressBarExample(self.percentage_Completed_task)
        self.container1.addWidget(circular_progress_widget_1)

        circular_progress_widget_2 = CircularProgressBarExample(self.percentage_Delayed_task)
        self.container2.addWidget(circular_progress_widget_2)

        circular_progress_widget_3 = CircularProgressBarExample(self.percentage_Urgent_task)
        self.container3.addWidget(circular_progress_widget_3)

        circular_progress_widget_4 = CircularProgressBarExample(self.percentage_Normal_task)
        self.container4.addWidget(circular_progress_widget_4)


class CircularProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.progress = 0

    def set_progress(self, percent):
        self.progress = min(percent, 100)  # Ensure progress does not exceed 100%
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Parameters
        width = self.width()
        height = self.height()
        size = min(width, height)
        margin = 0.08
        circle_radius = (size * (1 - margin)) / 2  # Calculate the radius dynamically

        # Background circle
        bg_gradient = QLinearGradient(self.rect().topLeft(), self.rect().bottomRight())
        bg_gradient.setColorAt(0, QColor("#ddd"))
        bg_gradient.setColorAt(1, QColor("#f0f0f0"))
        painter.setBrush(QBrush(bg_gradient))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(width / 2 - circle_radius, height / 2 - circle_radius, circle_radius * 2, circle_radius * 2)

        # Progress arc
        if self.progress <= 50:
            progress_angle = -self.progress * 3.6 / 2
        else:
            progress_angle = 90 + (-self.progress - 50) * 3.6 / 2

        progress_path = QPainterPath()
        progress_path.arcMoveTo(width / 2 - circle_radius, height / 2 - circle_radius, circle_radius * 2, circle_radius * 2, -90)
        progress_path.arcTo(width / 2 - circle_radius, height / 2 - circle_radius, circle_radius * 2, circle_radius * 2, -90, progress_angle)
        painter.drawPath(progress_path)

        # Highlight
        highlight_color = self.calculate_highlight_color()
        highlight_pen = QPen(QColor(highlight_color))
        highlight_pen.setWidth(6)
        painter.setPen(highlight_pen)

        # Calculate the highlight angle based on progress
        highlight_angle = progress_angle * 2
        highlight_path = QPainterPath()
        highlight_path.arcMoveTo(width / 2 - circle_radius, height / 2 - circle_radius, circle_radius * 2, circle_radius * 2, -90)
        highlight_path.arcTo(width / 2 - circle_radius, height / 2 - circle_radius, circle_radius * 2, circle_radius * 2, -90, highlight_angle)
        painter.drawPath(highlight_path)

        # Percentage text
        painter.setFont(QFont('Arial', 32, QFont.Bold))
        painter.drawText(width / 2 - circle_radius, height / 2 - circle_radius, circle_radius * 2, circle_radius * 2, Qt.AlignCenter, f'{self.progress}%')

    def calculate_highlight_color(self):
        progress = self.progress
        if progress <= 25:
            return "#ef233c"  # Red
        elif progress <= 50:
            return "#faa307"  # Yellow
        elif progress <= 75:
            return "#e76f51"  # Orange
        else:
            return "#588157"  # Green

class CircularProgressBarExample(QWidget):
    def __init__(self, progress_target=100):
        super().__init__()
        self.progress_target = progress_target
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Create a container widget to hold the circular progress bar
        container_widget = QWidget(self)
        layout.addWidget(container_widget)
        container_widget_layout = QVBoxLayout(container_widget)

        self.circular_progress_bar = CircularProgressBar(container_widget)  # Pass container_widget as parent
        container_widget_layout.addWidget(self.circular_progress_bar)

        # Calculate increment value based on target progress
        self.increment_value = 1 if self.progress_target <= 50 else (self.progress_target - 50) / 50

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(60)  

    def update_progress(self):
        # Increase progress
        if self.circular_progress_bar.progress < self.progress_target:
            new_progress = self.circular_progress_bar.progress + 1
            self.circular_progress_bar.set_progress(min(new_progress, self.progress_target))
        else:
            self.timer.stop()  


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())
