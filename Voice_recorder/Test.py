import sounddevice
from scipy.io.wavfile import write
from pydub import AudioSegment
import os
import shutil
from datetime import datetime
from tkinter import * 

from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image

root = Tk()
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
    
root.protocol("WM_DELETE_WINDOW", on_closing)

#check if MP4_FILE path exist , if not it will be created
a = os.path.isdir('MP4_FILES')
if a == True:
    pass
if a == False:
    os.mkdir('MP4_FILES')

def Audio_recording():
    #check date and time
    now = datetime.now()
    global dt_string
    #we will use this variable to name our file
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    #duration
    duration = 10
    #frame per secound
    fps = 44100
    print("Recording... ")
    recording = sounddevice.rec(int(duration*fps),samplerate=fps,channels=2)
    sounddevice.wait()
    write("output.wav",fps,recording)
    
#function to convert file from .wav to .mp3 and move it to the specific path
def convert(uncovertedFilesFolder):
    for file in os.scandir(uncovertedFilesFolder):
        if file.path.endswith(".wav"):
            convertedFile = os.path.splitext(os.path.basename(file.path))[0] + ".mp3"
            print("converting: ",file)
            AudioSegment.from_file(file.path).export(convertedFile,format="mp3")
            convertedFilesFolder = dt_string
            shutil.move(convertedFile,convertedFilesFolder)

def Test():
    Audio_recording()
    convert(uncovertedFilesFolder=os.chdir(os.getcwd()))
    shutil.move(dt_string,"MP4_FILES")
    os.remove("output.wav")
    print("done")



#boxy window or widget

img = (Image.open("001.png"))
re_img = img.resize((220,180))

#Icon1 = ImageTk.PhotoImage(Image.open("001.png"))
Icon1 = ImageTk.PhotoImage(re_img)

#creat a button
B = Button(root,text="clique me to record",image = Icon1,command=Test)
B.pack()

root.mainloop()