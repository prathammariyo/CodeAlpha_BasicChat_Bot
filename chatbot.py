"""CodeAlpha Task 4: Basic Chatbot
A simple rule-based chatbot.
Concepts: if-elif, functions, loops, input/output.
"""


def get_response(message):
    """Return a predefined reply based on the user's message."""
    msg = message.lower().strip()

    if msg in ("hello", "hi", "hey"):
        return "Hi!"
    elif msg == "how are you":
        return "I'm fine, thanks!"
    elif msg in ("what is your name", "your name", "who are you"):
        return "I'm CodeAlpha Bot."
    elif msg in ("help", "what can you do"):
        return "Try saying: hello, how are you, what is your name, or bye."
    elif msg in ("thanks", "thank you"):
        return "You're welcome!"
    elif msg in ("bye", "goodbye", "exit"):
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Type 'help' for options."


def main():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user = input("You: ")
        reply = get_response(user)
        print("Chatbot:", reply)
        if user.lower().strip() in ("bye", "goodbye", "exit"):
            break


if __name__ == "__main__":
    main()
