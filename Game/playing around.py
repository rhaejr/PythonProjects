import pyttsx3,time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak('Would you like to play a game?')
speak('if y, e, s spells yes, then what does e, y, e, s spell?')
for i in reversed(range(5)):
    speak(str(i+1))
    # time.sleep(1)
