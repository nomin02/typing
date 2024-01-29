import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar, QPushButton, QMenuBar, QMenu, QAction
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
import random

class TypingPracticeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.char_list = ['цүнх', 'гутал', 'алим', 'будаа']
        self.word_list = self.get_next_word_list()

        self.current_label = QLabel("", self)
        self.current_label.setFont(QFont("Helvetica", 36))

        self.next_label = QLabel("", self)
        self.next_label.setFont(QFont("Helvetica", 24))
        self.next_label.setStyleSheet("color: gray;")

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        
        self.hand_image_label = QLabel(self)  # 손 이미지를 표시할 QLabel
        hand_pixmap = QPixmap("hand_image.jpg")  # 사용할 이미지 파일의 경로를 넣어주세요
        self.hand_image_label.setPixmap(hand_pixmap)
        
        self.start_button = None
        
        layout = QVBoxLayout()
        
        layout.addWidget(self.current_label) # 현재 입력할 라벨
        layout.addWidget(self.next_label) # 다음에 입력할 라벨
        layout.addWidget(self.progress_bar) # 진행도 추가
        layout.addWidget(self.hand_image_label)  # 손 이미지 추가
        
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
            self.progress_bar.setValue(int((self.word_index / len(self.word_list)) * 100))
        else:
            self.current_label.setText("Дууссан")
            self.next_label.clear()
            self.progress_bar.setValue(100)
            self.create_start_button()

    def keyPressEvent(self, event):
        if self.start_button is None:
            user_input = event.text()
            if self.word_index < len(self.word_list):
                current_char = self.word_list[self.word_index]
                if user_input == current_char:
                    self.word_index += 1
                    self.show_char_practice()
                else:
                    self.current_label.setStyleSheet("color: red;")
                    self.timer.start(100)

    def reset_current_label_color(self):
        self.current_label.setStyleSheet("color: black;")
        self.timer.stop()
        
    def create_start_button(self):
        if self.start_button is None:
            self.start_button = QPushButton('다시 시작하기', self)
            self.start_button.clicked.connect(self.start_game)
            self.layout().addWidget(self.start_button)
        else:
            self.start_button.setEnabled(True)
            
    def start_game(self):
        self.word_index = 0
        self.start_button.setEnabled(False)
        self.show_char_practice()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TypingPracticeApp()
    window.setGeometry(300, 300, 640, 400)
    window.setWindowTitle("Үсэг")
    window.show()
    sys.exit(app.exec_())
