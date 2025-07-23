# Improved Simple ChatBot Program with keyword-based responses

# Response dictionary with multiple keywords pointing to one response
responses = {
    ("hi", "hello", "hey"): "Hi there! I'm ChatBot. How can I assist you today?",
    ("how are you", "how do you do"): "I'm just a chatbot, but I'm here to help you!",
    ("what is your name", "your name"): "You can call me ChatBot 😊",
    ("where are you from",): "I'm from the digital world, always ready to chat!",
    ("hobbies", "interests"): "My favorite thing is chatting with curious minds like you!",
    ("eat", "food", "hungry"): "I don't eat, but I can help you find tasty recipes.",
    ("color", "favourite color"): "I don't see colors, but blue seems popular!",
    ("music", "song"): "I can't hear music, but I can talk about it anytime!",
    ("recommend", "suggest"): "Sure! I can recommend books, movies, or music. What do you like?",
    ("thank you", "thanks"): "You're welcome!",
    ("bye", "goodbye", "exit", "quit"): "Bye! Take care and have a great day!"
}

# Function to get chatbot response
def get_bot_response(user_input):
    user_input = user_input.lower()
    for keywords, response in responses.items():
        for keyword in keywords:
            if keyword in user_input:
                return response
    return "I'm sorry, I didn't understand that. Can you rephrase?"

# Starting the chatbot
print("ChatBot: Hello! I'm ChatBot 🤖. Ask me anything or type 'bye' to exit.")

# Chat loop
while True:
    user_input = input("You: ").strip().lower()
    if any(exit_word in user_input for exit_word in ["bye", "exit", "quit", "goodbye"]):
        print("ChatBot: Goodbye! Have a nice day! 👋")
        break
    bot_reply = get_bot_response(user_input)
    print("ChatBot:", bot_reply)
