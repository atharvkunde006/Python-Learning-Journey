import datetime

print("AI Assistant Started 🤖")
print("Type: hi, time, date, help, exit")

while True:
    cmd = input("Enter command: ").lower()

    match cmd:

        case "hi":
            print("Hello Atharv 👋")

        case "time":
            now = datetime.datetime.now()
            print("Current time:", now.strftime("%H:%M:%S"))

        case "date":
            today = datetime.date.today()
            print("Today's date:", today)

        case "help":
            print("Available commands: hi, time, date, help, exit")

        case "exit":
            print("Assistant closed 🚀")
            break

        