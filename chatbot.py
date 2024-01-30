def simple_chatbot(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define predefined rules and responses
    greetings = ['hello', 'hi', 'hey', 'greetings']
    farewells = ['bye', 'goodbye', 'see you', 'farewell']
    questions = ['how are you', 'what is your name', 'who created you']
    
    # Check user input against predefined rules
    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I help you today?"

    elif any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a great day!"

    elif any(question in user_input for question in questions):
        return "I am just a simple chatbot. You can call me ECHO. I was created by Dhanush."

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask a different question?"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
