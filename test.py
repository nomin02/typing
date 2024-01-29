from PyQt5 import QtWidgets
from PyQt5 import QtCore
import random
import time

CHO = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 
    'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]
JUNG = [
    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 
    'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ'
]
JONG = [
    '', 'ㄱ','ㄲ','ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 
    'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 
    'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
]

WORD_LIST = [
    "남박사의 파이썬 프로그래밍 강좌 입니다.",
    "한글 타자 연습해서 타이핑 속도를 높여 보아요.",
    "파이썬은 코드가 짧고 유연하여 가독성과 생산성이 좋은 프로그래밍 언어 입니다.",
    "남박사의 파이썬 동영상 강좌는 인프런에서 볼 수 있습니다.",
    "독도는 우리땅"
]

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("남박사의 파이썬 타이핑게임")

        self.lb_next = QtWidgets.QLabel("다음 입력 연습 문장 입니다.", self)
        self.lb_next.setAlignment(QtCore.Qt.AlignLeft)
        self.lb_next.setStyleSheet("font-family:맑은 고딕;color:gray; font-size:16px;")
        
        self.lb_current = QtWidgets.QLabel("현재 입력 문장 입니다.", self)
        self.lb_current.setAlignment(QtCore.Qt.AlignLeft)
        self.lb_current.setStyleSheet("font-family:맑은 고딕;color:blue; font-size:20px;")

        self.lb_info = QtWidgets.QLabel("[속도:300.0 정확도: 100% 오타율: 0%]", self)
        self.lb_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info.setStyleSheet("font-family:맑은 고딕;color:gray; font-size:14px;")

        self.input = QtWidgets.QLineEdit(self)
        self.input.setFixedHeight(30)
        self.input.setStyleSheet("font-family:맑은 고딕;color:black; font-size:20px;")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lb_next)
        layout.addWidget(self.lb_current)
        layout.addWidget(self.input)
        layout.addWidget(self.lb_info)

        self.input.returnPressed.connect(self.enter_key)
        self.setLayout(layout)
        self.resize(650, 200)
        
        self.start_time = 0
        self.current_index = 0
        self.init_game()
        self.next_sentence()
        self.show()
    
    def break_korean(self, string):
        break_words = []
        for k in string:
            if ord("가") <= ord(k) <= ord("힣"):
                index = ord(k) - ord("가")
                c_cho = int((index / 28) / 21)
                c_jung = int((index / 28) % 21)
                c_jong = int(index % 28)

                break_words.append(CHO[c_cho])
                break_words.append(JUNG[c_jung])
                if c_jong > 0:
                    break_words.append(JONG[c_jong])
            else:
                break_words.append(k)
        return break_words

    def enter_key(self):
        duration = time.time() - self.start_time
        q = self.lb_current.text()
        u = self.input.text()
        break_q = self.break_korean(q)
        break_u = self.break_korean(u)
        correct = 0
        for c, a in zip(break_q, break_u):
            correct = correct + 1 if c == a else correct
        
        src_len = len(break_q)
        c = correct / src_len * 100
        e = (src_len - correct) / src_len * 100
        speed = float(correct / duration) * 60
        output = f"[속도:{speed:.1f} 정확도: {c:.2f}% 오타율: {e:.2f}%]"
        self.lb_info.setText(output)
        self.input.setText("")
        self.next_sentence()
        
    def init_game(self):
        random.shuffle(WORD_LIST)
        self.current_index = 0

    def next_sentence(self):
        if self.current_index < len(WORD_LIST):
            q = WORD_LIST[self.current_index]
            n = WORD_LIST[self.current_index + 1] if self.current_index + 1 < len(WORD_LIST) else ""
            
            self.lb_current.setText(q)
            self.lb_next.setText(n)
            self.start_time = time.time()
            self.current_index += 1
        else:
            reply = QtWidgets.QMessageBox.question(self, '타이핑게임', '모든남작 문제를 출제했습니다.\n다시 하시겠습니까?',
                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.Yes)
            if reply == QtWidgets.QMessageBox.Yes:
                self.init_game()
                self.next_sentence()
                self.input.setFocus()
            else:
                exit(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = MyWindow()
    app.exec_()