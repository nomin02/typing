import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton


class shortclass(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    def init_ui(self):
        label = QLabel("짧은 글 연습", self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = shortclass()
    window.setGeometry(300, 300, 640, 400)
    window.setWindowTitle("짧은 글 연습 화면")
    window.show()
    sys.exit(app.exec_())