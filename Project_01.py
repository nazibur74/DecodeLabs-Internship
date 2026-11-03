import string


def sanitize(text):
    text = text.lower()
    text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
    return " ".join(text.split())


def main():
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there!",
        "hey": "Hey! Nice to talk with you.",
        "how are you": "I'm doing well, thanks for asking!",
        "what is your name": "I'm Zinix, a rule-based AI chatbot.",
        "who created you": "I'm Zinix, a rule-based AI chatbot created by Nazibur Rahman.",
        "what can you do": "I can answer predefined questions.",
        "help": "Try: hello, hi, how are you, or what is your name.",
        "thank you": "You're welcome!",
        "thanks": "You're welcome!",
        "where are you from": "I'm from the digital world, created by Nazibur Rahman.",
        "what is your purpose": "My purpose is to assist users with predefined responses.",
        "i love you": "I appreciate your sentiment, but I'm just a chatbot."
    }

    exit_commands = ["bye", "exit", "quit"]

    print("=" * 40)
    print("Hi There, Welcome to Zinix!")
    print("Type 'help' for suggestions or 'bye' to exit.")
    print("=" * 40)

    while True:
        try:
            user_input = sanitize(input("\nYou: "))

            if not user_input:
                print("Zinix: Please enter a message.")
                continue
            if user_input in exit_commands:
                print("Zinix: Goodbye! Have a great day!")
                break

            reply = responses.get(user_input, "I don't understand that yet. Type 'help'.")
            print("Zinix:", reply)

        except (KeyboardInterrupt, EOFError):
            print("\nZinix: Goodbye! Have a great day!")
            break


if __name__ == "__main__":
    main()