print("Hello! I am a simple chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif user_input == "how are you":
        print("Bot: I'm doing well, just helping humans!")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
