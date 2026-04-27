import win32com.client as win
import datetime
speaker = win.Dispatch("SAPI.SpVoice")
while True:
    a = input("Enter command: ")
    if a == "hello":
     speaker.Speak("Hello Atharv bhai")
    elif a == "how are you":
     speaker.Speak("I am fine, what about you bro")
    elif a == "i want spend time with you":
     speaker.Speak("Yes sure, I am here for you, ask me anything")
    elif a == "what is time right now":
     current_time = str(datetime.datetime.now())
     speaker.Speak(current_time)
    else:
        speaker.Speak("Sorry, invalid command")