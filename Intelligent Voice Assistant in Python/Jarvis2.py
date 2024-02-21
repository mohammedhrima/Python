from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import nltk



recongnizer = speech_recognition.Recognizer()
speaker = tts.init()
speaker.setProperty('rate',150)

todo_list = ['Go Shopping','Clean room','Record a Video']


def creat_note():
    global recongnizer

    speaker.say("Hello buddy")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:

                recongnizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recongnizer.listen(mic)

                note = recongnizer.recongnize_google(audio)
                note = note.lower()

                speaker.say("choose a file name")
                speaker.runAndWait()

                recongnizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recongnizer.listen(mic)

                fillename = recongnizer.recognize_google(audio)
                fillename = fillename.lower()
            with open(fillename,'w') as f:
                f.write(note)
                done = True
                speaker.sayf("I creat successfully the note {filename}")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recongnizer = speech_recognition.Recognizer()
            speaker.say("Please say again")
            speaker.runAndWait()
            pass

def add_todo():
    global recongnizer
    speaker.say("What todod do you want to add? ")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recongnizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recongnizer.listen(mic)
                item = recongnizer.recongnize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say(f"I added {item} to the todo list!")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recongnizer = speech_recognition.Recognizer()
            speaker.say("I didn't get you")
            speaker.runAndWait()

def show_todos():
    speaker.say("the items on your list are")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    speaker.say("Hello what can I do for you")
    speaker.runAndWait()

def quit():
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)

mappings = {
    "greeting": hello,
    "creat_note": creat_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit":quit
}


assistant = GenericAssistant('intents.json',intent_methods=mappings)
assistant.train_model()

#assistant.request("How are you?")

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recongnizer.adjust_for_ambient_noise(mic,duration=0.2)
            audio = recongnizer.listen(mic)
            message = message.lower()
        assistant.reques(message)
    except speech_recognition.UnknownValueError:
        recongnizer = speech_recognition.Recognizer()
        