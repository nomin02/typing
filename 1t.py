import tkinter 
from tkinter import ttk

window = tkinter.Tk()
window.title("Mongolia typing test")
window.geometry("640x400+100+100")
window.resizable(False, False)

def confirm(event):
    in_text = ""+str(input_text.get())
    label.configure(text = in_text)
#바뀔 라벨
label = tkinter.Label(window, text="text?")
label.pack()
#입력창
input_text = tkinter.Entry(window, width = 30)
input_text.bind("return", confirm())
input_text.pack()
#버튼
button = tkinter.Button(window, text = "계산", command = confirm)
button.pack()

window.mainloop()