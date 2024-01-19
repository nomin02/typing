import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class longclass(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    def init_ui(self):
        label = QLabel("긴 글 연습", self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = longclass()
    window.setGeometry(300, 300, 640, 400)
    window.setWindowTitle("긴 글 연습 화면")
    window.show()
    sys.exit(app.exec_())