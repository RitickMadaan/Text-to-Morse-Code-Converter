from tkinter import *
window = Tk()
window.title('Hello Python')
window.geometry("400x300+10+20")


def printText():
    inp = inputBox.get(1.0, "end-1c")
    lbl.config(text="Morse Code: "+inp)


welcome = Label(window, text="Welcome to Morse Code Converter")
welcome.place(x=100, y=10)

inputBox = Text(
    window,
    height=2,
    width=37
)

inputBox.place(x=50, y=50)

printButton = Button(
    window,
    text="Convert to morse",
    command=printText
)
printButton.place(x=150, y=100)

lbl = Label(window, text="")
lbl.place(relx=0.5, rely=0.7, anchor='center')

window.mainloop()
