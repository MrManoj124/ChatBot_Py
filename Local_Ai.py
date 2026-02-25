print("🤖 Local AI Chatbot Started!")
print("Type 'exit' to quit.\n")

While True:
    user_input = input("You : ").lower()

    if user_input == "Exit" :
    print("Bot : Goodbye!")
    break

    elif "hello" in user_input:
        print("Bot : Hi there!")

    elif "how are you" in user_input:
        print("Bot : I'm just code , but I'm functioning perfectly!")

    elif"your name" in user_input:
        print("Bot : I am your Local AI Assistant.")

    else:
        print("Bot : I don't understand that yet.")


responses = {
    "hello" : "Hi there!",
    "hi" : "Hello!",
    "bye" : "Goodbye!",
    "help" : "I can answer basic questions."
}

while True : 
    user_input = input("You : ").lower()

    