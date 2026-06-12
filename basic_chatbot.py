from datetime import datetime

print("🤖 Smart Python Chatbot")
print("Type 'bye' to exit.\n")

name = input("Bot: What is your name? ")
print(f"Bot: Hello {name}! Nice to meet you.\n")

responses = {
    "hello": f"Hi {name}! How can I help you?",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I am a Smart Python Chatbot.",
    "who created you": "Sai Santhana Lakshmiwh created me.",
    "thank you": "You're welcome!",
    "good morning": f"Good Morning {name}!",
    "good night": f"Good Night {name}!"
}

while True:
    user_input = input(f"{name}: ").lower()

    if user_input == "bye":
        print(f"Bot: Goodbye {name}! Have a wonderful day.")
        break

    elif user_input == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current Time =", current_time)

    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's Date =", current_date)

    elif user_input in responses:
        print("Bot:", responses[user_input])

    else:
        print("Bot: Sorry, I don't understand that. Try saying hello, date, time, or bye.")