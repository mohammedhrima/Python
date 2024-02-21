import eel
import eel.browsers
from numpy import size
import sounddevice
import soundfile
import os
from datetime import datetime
import queue
import threading
import glob
import shutil
import sys
import winsound
import ctypes

"----------------------Remove all wav file----------------------"


def RemoveWav():
    for bfile in os.listdir():
        bfile = str(bfile)
        if bfile.endswith('.wav'):
            try:
                os.remove(bfile)
            except WindowsError:
                if WindowsError == 5:
                    os.chmod(bfile, 0o777)
                    try:
                        os.remove(bfile)
                    except WindowsError:
                        raise WindowsError
                else:
                    raise WindowsError
    print("after remove")


RemoveWav()

"----------------------Check if Consigne LPF path exist----------------------"
Consigne_Folder = os.path.isdir('Consigne LPF')
if Consigne_Folder == True:
    pass
if Consigne_Folder == False:
    os.mkdir('Consigne LPF')

print("after check consigne lpf path")

audio_container = queue.Queue()
eel.init("src")

# to send data from python to javascript

global num


@eel.expose
def get_Matricule(Mat):
    print("line 69 in python", Mat)
    Mat = str(Mat)
    Database_file = open("DATABASE\\Matricules.txt", "r").read()
    #print("line 73", Database_file)
    #print("line 73", type(Database_file))
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
            with soundfile.SoundFile(dt_string, mode='w', samplerate=44100, channels=2) as file:
                with sounddevice.InputStream(samplerate=44100, channels=2, callback=callback):
                    while Recor_ding == True:
                        print("recording")
                        file.write(audio_container.get())
        except:
            sys.exit(1)
    if x == "start":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        RemoveWav()
        print("start recording")
        now = datetime.now()
        global dt_string
        dt_string = now.strftime("%Y-%m-%d_%Hh%Mm%Ss("+num+").wav")
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
            winsound.PlaySound(
                dt_string, winsound.SND_ASYNC | winsound.SND_ALIAS)

    elif x == "save":
        winsound.PlaySound(None, winsound.SND_ASYNC)
        print("save recording")
        source_dir = os.getcwd()
        dst = os.getcwd() + '\\Consigne LPF'
        files = glob.iglob(os.path.join(source_dir, "*.wav"))
        for file in files:
            if os.path.isfile(file):
                shutil.copy2(file, dst)
        if os.path.isfile(dt_string):
            os.remove(dt_string)
    else:
        print("line 75")


@eel.expose
def Exist():
    print("From exist")
    List = []
    for Soundfile in os.listdir("Consigne LPF"):
        Soundfile = str(Soundfile)
        if Soundfile.endswith(".wav"):
            print(Soundfile)
            Soundfile = Soundfile.replace(".wav", "")
            List.append(Soundfile)
    return List


@eel.expose
def PlayHist(file):
    if os.path.isfile(file):
        winsound.PlaySound(None, winsound.SND_ASYNC)
        winsound.PlaySound(
            file, winsound.SND_ASYNC | winsound.SND_ALIAS)


eel.start("main.html", size=(540, 900))
