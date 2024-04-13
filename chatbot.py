import openai

# Set up OpenAI API with your API key
openai.api_key = "#####"

def get_mental_health_support(user_input):
    # Define initial conversation
    if user_input.lower() == "hi":
        return "Hello! I'm here to provide mental health support. How can I help you today?"
    
    # Define specific conversation flows
    if "stress" in user_input.lower():
        return (
            "It sounds like you're experiencing stress. I'm here to help."
            "\n- Would you like some breathing exercises?"
            "\n- Or would you like me to share some resources on stress management?"
        )
    
    if "anxiety" in user_input.lower():
        return (
            "It sounds like you're experiencing anxiety. I'm here to help."
            "\n- Would you like some grounding techniques?"
            "\n- Or would you like me to share resources on managing anxiety?"
        )
    
    if "depression" in user_input.lower():
        return (
            "It sounds like you're experiencing depression. I'm here to help."
            "\n- Would you like some mindfulness exercises?"
            "\n- Or would you like me to share resources on managing depression?"
        )
    
    # If input is not understood, return a general message
    return "I'm here to help with mental health support. Can you please tell me more about what you're experiencing?"

def chat_with_user():
    print("Welcome to the mental health support chatbot!")
    while True:
        user_input = input("You: ")
        
        # If user says goodbye, end the conversation
        message =user_input
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot: Take care! Remember, you are not alone.")
            break
        
        # Get the chatbot's response based on user input
        response = get_mental_health_support(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot conversation
chat_with_user()
