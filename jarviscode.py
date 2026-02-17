if'email to harry'in query:
try:
    speak("What should i say?")
    content=takecommand()
    to="harryyourEmail@gmail.com"
    sendEmail(to,content)
    speak("Email has been sent!")
except Exception as e:
    print(e)
    speak("sorry my freind harry bhai. i am not able to send this mail")
else:
    print("No query matched")