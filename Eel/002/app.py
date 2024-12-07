import eel
import os
import sounddevice as sd
import soundfile as sf
import queue
import threading
import shutil
import glob
from datetime import datetime
import pygame 

pygame.mixer.init()

Consigne_Folder = 'Consigne LPF'
if not os.path.isdir(Consigne_Folder):
    os.mkdir(Consigne_Folder)

audio_container = queue.Queue()
eel.init("src")

global num

@eel.expose
def get_Matricule(Mat):
    print("line 69 in python", Mat)
    Mat = str(Mat)
    Database_file = open("DATABASE/Matricules.txt", "r").read()
    if Mat in Database_file:
        num = Mat
        print("exit")
        return True
    return False

@eel.expose
def Voice_Rec_Stop(x, y):
    if y != "":
        num = y

    def Record_audio():
        def callback(indata, frames, time, status):
            audio_container.put(indata.copy())
        try:
            global Recor_ding
            Recor_ding = True
            with sf.SoundFile(dt_string, mode='w', samplerate=44100, channels=2) as file:
                with sd.InputStream(samplerate=44100, channels=2, callback=callback):
                    while Recor_ding == True:
                        print("recording")
                        file.write(audio_container.get())
        except Exception as e:
            print(f"Error during recording: {e}")
            sys.exit(1)

    if x == "start":
        print("start recording")
        now = datetime.now()
        global dt_string
        dt_string = now.strftime(f"%Y-%m-%d_%Hh%Mm%Ss({num}).wav")
        R = threading.Thread(target=Record_audio)
        R.start()
        global file_exists
        file_exists = True

    elif x == "pause":
        print("pause recording")
        if file_exists:
            global Recor_ding
            Recor_ding = False
            file_exists = False

    elif x == "listen":
        print("listen to recording")
        if os.path.isfile(dt_string):
            pygame.mixer.music.load(dt_string)
            pygame.mixer.music.play()

    elif x == "save":
        print("save recording")
        source_dir = os.getcwd()
        dst = os.path.join(os.getcwd(), 'Consigne LPF')
        files = glob.iglob(os.path.join(source_dir, "*.wav"))
        for file in files:
            if os.path.isfile(file):
                shutil.copy2(file, dst)
        if os.path.isfile(dt_string):
            os.remove(dt_string)
    else:
        print("Invalid command")

@eel.expose
def Exist():
    print("From Exist")
    List = []
    for Soundfile in os.listdir(Consigne_Folder):
        if Soundfile.endswith(".wav"):
            Soundfile = Soundfile.replace(".wav", "")
            List.append(Soundfile)
    return List

@eel.expose
def PlayHist(file):
    if os.path.isfile(file):
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

eel.start("main.html", size=(540, 900))
