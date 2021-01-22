import playAudio


def playAudio(code):
    for i in code:
        if(i == '.'):
            playAudio('srcs\Beep-1.mp3')
            # play audio file for .
        elif(i == '_'):
            playAudio('srcs\Beep-2.mp3')
            # play audio file for _
