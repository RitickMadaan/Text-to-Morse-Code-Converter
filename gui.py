from Convert import convert
from PlayAudioFiles import playAudioFiles

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


def playMorseAudio():
    inp = inputBox.get(1.0, "end-1c")
    code = convert(inp)
    playAudioFiles(code)

# TODO:get code output and play audio based on morse code


welcome = Label(window, text="Welcome to Morse Code Converter")
welcome.place(relx=0.5, rely=0.09, anchor='center')

inputBox = Text(
    window,
    height=2,
    width=37
)

inputBox.place(relx=0.5, rely=0.23, anchor='center')

convertButton = Button(
    window,
    text="Convert to morse",
    command=printText
)
convertButton.place(relx=0.5, rely=0.4, anchor='center')

lbl = Label(window, text="")
lbl.place(relx=0.5, rely=0.55, anchor='center')

adudioButton = Button(
    window,
    image=photo,
    command=playMorseAudio
)

adudioButton.place(relx=0.5, rely=0.8, anchor='center')


window.mainloop()
