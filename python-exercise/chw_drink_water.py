import time
import win32com.client as win
from plyer import notification

speaker = win.Dispatch("SAPI.SpVoice")

REPEAT_INTERVAL = 3600  # 1 hour

while True:
    message = "Hey Atharv, drink water"

    speaker.Speak(message)

    notification.notify(
        title="Water Reminder",
        message=message,
        timeout=5
    )

    time.sleep(REPEAT_INTERVAL)