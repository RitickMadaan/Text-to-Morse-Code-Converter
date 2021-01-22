import convert
import playAudio

from tkinter import *
window = Tk()
window.title('Hello Python')
window.geometry("400x300+10+20")

photo = PhotoImage(file=r"srcs\audioImage.png")
photo = photo.subsample(6, 6)


def printText():
    inp = inputBox.get(1.0, "end-1c")
    code = convert(inp)
    lbl.config(text="Morse Code: "+code)

# TODO:get code output and play audio based on morse code


welcome = Label(window, text="Welcome to Morse Code Converter")
welcome.place(x=100, y=10)

inputBox = Text(
    window,
    height=2,
    width=37
)

inputBox.place(x=50, y=50)

convertButton = Button(
    window,
    text="Convert to morse",
    command=printText
)
convertButton.place(x=150, y=100)

lbl = Label(window, text="")
lbl.place(relx=0.5, rely=0.55, anchor='center')

adudioButton = Button(
    window,
    image=photo,
)
adudioButton.place(relx=0.5, rely=0.8, anchor='center')


window.mainloop()
