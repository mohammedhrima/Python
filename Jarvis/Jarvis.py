import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)

def talk(text):
    #engine.say('I am you assistant')
    #engine.say('What can I do for you')
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command: 
                command = command.replace('jarvis','')
                print(command)
    except:
        pass
    return command


def run_jarvis():
    while True:
        command = take_command()
        #print(command)
        if 'play' in command:
            song = command.replace('play','playing')
            talk(song)
            print(song)
            pywhatkit.playonyt(song)
        elif 'search for' in command:
            search = command.replace('search for','')
            info = wikipedia.summary(search,1)
            print(info)
            talk(info)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk("it's "+time)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'close chrome' in command:
            print('closing chrome...')
            os.system("taskkill /im chrome.exe /f")
        elif 'stop' in command:
            talk('okey sir , see you soon')
            return False
        else:
            pass
run_jarvis()