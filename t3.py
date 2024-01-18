import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import QTimer
import random

class TypingPracticeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.char_list = ['й', 'ы', 'б', 'ө']
        self.word_list = self.get_next_word_list()

        self.current_label = QLabel("", self)
        self.current_label.setFont(QFont("Helvetica", 36))

        self.next_label = QLabel("", self)
        self.next_label.setFont(QFont("Helvetica", 24))
        self.next_label.setStyleSheet("color: gray;")

        layout = QVBoxLayout()
        layout.addWidget(self.current_label)
        layout.addWidget(self.next_label)

        self.setLayout(layout)

        self.word_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.reset_current_label_color)

        self.show_char_practice()

    def get_next_word_list(self):
        return random.sample(self.char_list * 7, 7)

    def show_char_practice(self):
        if self.word_index < len(self.word_list):
            current_char = self.word_list[self.word_index]
            next_chars = " ".join(self.word_list[self.word_index + 1:self.word_index + 4])
            self.current_label.setText(current_char)
            self.next_label.setText(next_chars)
        else:
            self.current_label.setText("Дууссан")
            self.next_label.clear()

    def keyPressEvent(self, event):
        user_input = event.text()
        if self.word_index < len(self.word_list):
            current_char = self.word_list[self.word_index]
            if user_input == current_char:
                self.word_index += 1
                self.show_char_practice()
            else:
                self.current_label.setStyleSheet("color: red;")
                self.timer.start(100)  # 0.1초 후에 reset_current_label_color 메소드 호출

    def reset_current_label_color(self):
        self.current_label.setStyleSheet("color: black;")
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TypingPracticeApp()
    window.setGeometry(300, 300, 640, 400)
    window.setWindowTitle("Үсэг")
    window.show()
    sys.exit(app.exec_())
