import tkinter as tk
import random

class TypingPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тренировка по печати")

        # 화면 크기를 640x400으로 설정
        self.root.geometry("640x400")

        # GUI의 정중앙 위치 계산
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        gui_width = 640
        gui_height = 400
        x = (screen_width - gui_width) // 2
        y = (screen_height - gui_height) // 2 - 50  # 약간 위로 이동

        # GUI의 위치를 설정
        self.root.geometry(f"{gui_width}x{gui_height}+{x}+{y}")

        self.char_list = ['й', 'ы', 'б', '\u04e9']
        self.word_list = self.get_next_word_list()

        self.word_frame = tk.Frame(root)
        self.word_frame.pack(pady=20)

        self.current_label = tk.Label(self.word_frame, text="", font=("Ariel", 36))
        self.current_label.grid(row=0, column=0)

        self.next_label = tk.Label(self.word_frame, text="", font=("Helvetica", 24), fg="gray")
        self.next_label.grid(row=0, column=1, padx=10)

        self.word_index = 0

        self.root.bind('<Key>', self.on_key_press)
        self.show_char_practice()

    def get_next_word_list(self):
        return random.sample(self.char_list * 7, 7)

    def show_char_practice(self):
        if self.word_index < len(self.word_list):
            current_char = self.word_list[self.word_index]
            next_chars = " ".join(self.word_list[self.word_index + 1:self.word_index + 4])
            self.current_label.config(text=current_char)
            self.next_label.config(text=next_chars, fg="gray")
        else:
            self.current_label.config(text="Тренировка по местам закончилась.")
            self.next_label.config(text="")

    def on_key_press(self, event):
        user_input = event.char
        if self.word_index < len(self.word_list):
            current_char = self.word_list[self.word_index]
            if user_input == current_char:
                self.word_index += 1
                self.show_char_practice()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingPracticeApp(root)
    root.mainloop()
