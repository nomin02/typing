import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from jari_typing_practice_app2 import TypingPracticeApp # Assuming your TypingPracticeApp class is in a file named typing_practice_app.py
from word_typing_practice_app2 import wordclass
from short_typing_practice_app2 import shortclass
from long_typing_practice_app2 import longclass

class MainClass(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        label = QLabel("타자 연습", self)

        button1 = QPushButton("자리 연습", self)
        button1.clicked.connect(self.launch_typing_practice)

        button2 = QPushButton("단어 연습", self)
        button2.clicked.connect(self.launch_word_practice)
        
        button3 = QPushButton("짧은 글 연습", self)
        button3.clicked.connect(self.launch_short_practice)
        
        button4 = QPushButton("긴 글 연습", self)
        button4.clicked.connect(self.launch_long_practice)
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        self.setLayout(layout)

    def launch_typing_practice(self):
        self.typing_practice_app = TypingPracticeApp()
        self.typing_practice_app.setGeometry(300, 300, 640, 400)
        self.typing_practice_app.show()
    def launch_word_practice(self):
        self.typing_practice_app = wordclass()
        self.typing_practice_app.setGeometry(300, 300, 640, 400)
        self.typing_practice_app.show()
    def launch_short_practice(self):
        self.typing_practice_app = shortclass()
        self.typing_practice_app.setGeometry(300, 300, 640, 400)
        self.typing_practice_app.show()
    def launch_long_practice(self):
        self.typing_practice_app = longclass()
        self.typing_practice_app.setGeometry(300, 300, 640, 400)
        self.typing_practice_app.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    window.setGeometry(300, 300, 640, 400)
    window.setWindowTitle("메인화면")
    window.show()
    sys.exit(app.exec_())
