import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import os
import shutil
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image
import threading

# Check if MP4_FILES folder exists, create it if not
mp4_files_dir = 'MP4_FILES'
os.makedirs(mp4_files_dir, exist_ok=True)

# Tkinter Window Setup
root = Tk()
root.title("Voice Recorder")

# Global variables for recording state
is_recording = False
recording_data = None
duration = 10  # Set recording duration to 10 seconds for each start
fps = 44100  # Set frames per second
current_file = None

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def audio_recording():
    """Function to record audio and save as a .wav file."""
    global is_recording, recording_data, current_file
    if not is_recording:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H-%M-%S")  # Use valid filename format

        print("Recording...")
        is_recording = True
        recording_data = sd.rec(int(duration * fps), samplerate=fps, channels=2, dtype='int16')
        sd.wait()

        wav_filename = f"{dt_string}.wav"
        write(wav_filename, fps, recording_data)
        current_file = wav_filename
        print(f"Recording saved as {wav_filename}")
        return wav_filename, dt_string
    else:
        print("Recording is already in progress.")

def convert_to_mp3(wav_filename, dt_string):
    """Converts .wav file to .mp3 and moves it to the MP4_FILES folder."""
    try:
        mp3_filename = os.path.splitext(wav_filename)[0] + ".mp3"
        print(f"Converting {wav_filename} to {mp3_filename}...")

        # Convert to mp3 using pydub
        AudioSegment.from_wav(wav_filename).export(mp3_filename, format="mp3")

        # Move the converted mp3 file to the MP4_FILES folder
        mp3_dest = os.path.join(mp4_files_dir, dt_string)
        os.makedirs(mp3_dest, exist_ok=True)  # Ensure destination folder exists
        shutil.move(mp3_filename, mp3_dest)

        # Remove original wav file after conversion
        os.remove(wav_filename)
        print(f"Conversion complete, file saved to {mp3_dest}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        messagebox.showerror("Error", f"An error occurred during conversion: {e}")

def stop_recording():
    """Stop the current recording process."""
    global is_recording, recording_data, current_file
    if is_recording:
        is_recording = False
        print("Recording stopped.")
        convert_to_mp3(current_file, current_file.split('.')[0])

def start_recording():
    """Start a new recording thread."""
    threading.Thread(target=audio_recording, daemon=True).start()

def toggle_recording():
    """Toggle between start and stop."""
    if is_recording:
        stop_recording()
    else:
        start_recording()

# Load and resize icon image for the button
img = Image.open("001.png")
re_img = img.resize((220, 180))
icon = ImageTk.PhotoImage(re_img)

# Create and pack the start/pause/stop button
B = Button(root, text="Start/Stop Recording", image=icon, compound=TOP, command=toggle_recording)
B.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
