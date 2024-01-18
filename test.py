import tkinter as tk
import random

class TypingPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("타자 연습")

        self.char_list = ["ㅁ", "ㄴ", "ㅇ", "ㄹ", "ㅓ", "ㅏ", "ㅣ", ";"]

        self.current_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.current_label.pack(pady=20)

        self.char_button = tk.Button(root, text="자리 연습", command=self.show_char_practice)
        self.char_button.pack()

        self.current_word = ""
        self.show_char_practice()

        self.root.bind('<Key>', self.on_key_press)

    def get_random_char(self):
        return random.choice(self.char_list)

    def show_char_practice(self):
        self.current_word = self.get_random_char()
        self.current_label.config(text=self.current_word)

    def on_key_press(self, event):
        user_input = event.char
        if user_input == self.current_word[0]:
            self.current_word = self.current_word[1:]
            if not self.current_word:
                self.show_char_practice()
            else:
                self.current_label.config(text=self.current_word)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mongolia typing test")
    root.geometry("640x400+100+100")
    root.resizable(False, False)
    app = TypingPracticeApp(root)
    root.mainloop()
