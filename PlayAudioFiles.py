from playsound import playsound
import time


def playAudioFiles(code):
    for i in code:
        if(i == '.'):
            playsound('srcs\Beep-1.mp3')
            # play audio file for .
        elif(i == '-'):
            playsound('srcs\Beep-2.mp3')
            # play audio file for _
        elif(i == '/'):
            time.sleep(1)
