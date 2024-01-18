import tkinter as tk
from tkinter import messagebox
import random
def check_answer():
    user_input = entry.get()
    correct_answer = "타자연습"  # 실제 자리 연습에 사용될 정답 문자열

    if user_input == correct_answer:
        messagebox.showinfo("정답", "정답입니다!")
    else:
        messagebox.showerror("오답", "오답입니다. 다시 시도하세요.")

def show_place_practice():
    word_button.pack_forget()  # "자리 연습" 버튼을 화면에서 숨김
    place_frame.pack()

    label.config(text="타자 연습을 시작하세요:")
    entry.delete(0, tk.END)  # 입력 필드 초기화
    entry.focus()  # 입력 필드에 포커스 설정

root = tk.Tk()
root.title("Mongolia typing test")
root.geometry("640x400+100+100")
root.resizable(False, False)

word_frame = tk.Frame(root)

place_frame = tk.Frame(root)
label = tk.Label(place_frame, text="")
label.pack()

entry = tk.Entry(place_frame)
entry.pack()

check_button = tk.Button(place_frame, text="확인", command=check_answer)
check_button.pack()

word_button = tk.Button(root, text="자리 연습", command=show_place_practice)
word_button.pack()

root.mainloop()
