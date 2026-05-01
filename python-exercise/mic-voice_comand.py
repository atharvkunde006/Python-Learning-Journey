import speech_recognition as sr
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import datetime

# 🔊 Initialize voice engine
engine = pyttsx3.init()

# 🔥 Voice settings
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # 0 = male, 1 = female
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

# 🔊 Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# 🎤 Record audio
def record_audio(filename="input.wav", duration=5, fs=44100):
    print("Listening...")
    
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()

    # 🔥 convert float → int16 (VERY IMPORTANT)
    recording = np.int16(recording * 32767)

    write(filename, fs, recording)

# 🧠 Convert speech to text
def take_command():
    r = sr.Recognizer()

    record_audio()

    with sr.AudioFile("input.wav") as source:
        audio = r.record(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except:
        print("Could not understand")
        return "none"

# 🔊 Greeting at start
def greet():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good morning Atharv")
    elif hour < 18:
        speak("Good afternoon Atharv")
    else:
        speak("Good evening Atharv")

    speak("Main tumhara voice assistant hoon. Batao kya karna hai?")

# 🚀 MAIN PROGRAM
greet()

while True:
    command = take_command()

    if "hello" in command:
        speak("Hello Atharv, kaise ho?")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"Abhi time hai {time}")

    elif "your name" in command:
        speak("Mera naam Jarvis hai")

    elif "exit" in command:
        speak("Goodbye Atharv")
        break

    elif command == "none":
        speak("Sorry, mujhe samajh nahi aaya")