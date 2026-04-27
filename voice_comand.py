import win32com.client as win
speaker=win.Dispatch("SAPI.SpVoice")
list=["Atharv" , "kunal", "sarthak","vikas" ]
for name in list:
    shoutout=f"jay bhim {[name]}"
    print(shoutout)
    speaker.speak(shoutout)
    
    