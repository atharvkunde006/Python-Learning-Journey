import win32com.client as win
import time
speaker=win.Dispatch("SAPI.SpVoice")
time=time.sleep(5)
a=f"just wait for drink"
print(a)
speaker.Speak(a)