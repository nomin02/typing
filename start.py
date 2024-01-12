import tkinter

window = tkinter.Tk()

window.title("Mongolia typing test")
window.geometry("640x400+100+100")
window.resizable(False, False)

count = 0

def countUP():
    global count
    count +=1
    label.config(text = str(count))

label = tkinter.Label(window, text = "Typing Practice", font = ("Arial", 30))
label.pack()

button = tkinter.Button(window, text = "자리 연습", overrelief="solid", width = 15, repeatdelay=1000, repeatinterval=100, padx=100, pady = 30, bg = "gray", fg = "black")
button.pack()
window.mainloop()