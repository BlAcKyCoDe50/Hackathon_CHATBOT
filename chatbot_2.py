import openai

# Set up OpenAI API with your API key
openai.api_key = "####"  # Replace with your API key

# Keep track of conversation context
messages = [
    {"role": "system", "content": "You are a helpful mental health support chatbot."}
]

def chat_with_user():
    print("Welcome to the mental health support chatbot!")
    while True:
        user_input = input("You: ")

        # If user says goodbye, end the conversation
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot: Take care! Remember, you are not alone.")
            break

        # Add user input to the conversation context
        messages.append({"role": "user", "content": user_input})

        # Call ChatGPT API to get a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Get the reply from the API response
        reply = response["choices"][0]["message"]["content"]

        # Add the chatbot's reply to the conversation context
        messages.append({"role": "assistant", "content": reply})

        # Print the chatbot's reply
        print(f"Chatbot: {reply}")

# Start the chatbot conversation
chat_with_user()
