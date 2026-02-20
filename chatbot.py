print("Simple Chatbot 🤖 started")
print("Type: hi, who are you, help, bye")

while True:
    msg = input("You: ")

    match msg:

        case "hi":
            print("Bot: Hello Atharv 👋")

        case "who are you":
            print("Bot: I am your Python chatbot 🤖")

        case "help":
            print("Bot: You can type hi, who are you, help, bye")

        case "bye":
            print("Bot: Goodbye 🚀")
            break

        case _:
            print("Bot: I don't understand ❌")