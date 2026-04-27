import win32com.client as win
import time
speaker=win.Dispatch("SAPI.Spvoice")
time.sleep(3)
alaram=f"tring tring tring wake up bro this is morning now"
print(alaram)
speaker.speak(alaram)