import random
from datetime import datetime

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the Python programmer calm? Because they kept their exceptions handled!",
    "Debugging: Being the detective in a crime movie where you are also the criminal."
]

quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Believe in yourself and all that you are.",
    "Every expert was once a beginner."
]


def greeting():
    hour = datetime.now().hour

    if hour < 12:
        return "Good Morning"
    elif hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"


def calculator():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+ - * /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", num1 / num2)
        else:
            print("Invalid operator.")
    except:
        print("Invalid input.")


def chatbot():

    print("=" * 50)
    print("      CODEALPHA BASIC CHATBOT")
    print("=" * 50)

    name = input("What is your name? ")

    print(f"\nBot: {greeting()}, {name}! 😊")
    print("Type 'help' to see what I can do.\n")

    while True:

        user = input(f"{name}: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print(f"Bot: Hello {name}! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user == "your name":
            print("Bot: I am CodeAlpha ChatBot.")

        elif user == "date":
            print("Bot:", datetime.now().strftime("%d-%m-%Y"))

        elif user == "time":
            print("Bot:", datetime.now().strftime("%I:%M:%S %p"))

        elif user == "joke":
            print("Bot:", random.choice(jokes))

        elif user == "motivate":
            print("Bot:", random.choice(quotes))

        elif user == "calculate":
            calculator()

        elif user == "guess":
            number = random.randint(1, 10)
            guess = int(input("Guess a number (1-10): "))

            if guess == number:
                print("Bot: 🎉 Correct!")
            else:
                print(f"Bot: Wrong! The number was {number}")

        elif user in ["thanks", "thank you"]:
            print("Bot: You're welcome!")

        elif user in ["good", "awesome", "great"]:
            print("Bot: Thank you! 😊")

        elif user == "help":
            print("""
I can do the following:

hello
how are you
your name
date
time
joke
motivate
calculate
guess
thanks
bye
""")

        elif user == "bye":
            print(f"Bot: Goodbye, {name}! Have a wonderful day. 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that command.")


chatbot()