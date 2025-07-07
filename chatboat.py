def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm functioning well. Thanks!")
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot, your virtual assistant.")
        elif "help" in user_input:
            print("Chatbot: I can chat with you, tell you my name, or say goodbye. Try asking something!")
        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
