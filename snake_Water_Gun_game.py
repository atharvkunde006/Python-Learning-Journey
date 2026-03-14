import random

def check_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "User Wins"
    else:
        return "Computer Wins"

options = ["snake", "water", "gun"]

user = input("Enter snake, water, or gun: ").lower()
computer = random.choice(options)

print("Computer chose:", computer)

result = check_winner(user, computer)
print("Result:", result)