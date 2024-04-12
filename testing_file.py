import openai

# Set up OpenAI API with your API key
openai.api_key = "63f4009c83msh2d10a9ad70f7b08p15d51cjsn927c0f92b533"

# Define the mental health support function
def get_mental_health_support(user_input):
    if user_input.lower() == "hi":
        return "Hello! I'm here to provide mental health support. How can I help you today?"
    
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
    if "I'm feeling overwhelmed with stress. Can you help?" in user_input.lower():
        return(
            "Absolutely! Let's start with some breathing exercises to help you relax."
        )
    if "How do I manage stress at work?" in user_input.lower():
        return (
            "Try taking short breaks, prioritizing tasks, and setting clear boundaries between work and personal life."
        )
    
    return "I'm here to help with mental health support. Can you please tell me more about what you're experiencing?"

# Chatbot function
def chat_with_user():
    print("Welcome to the mental health support chatbot!")
    
    messages = []
    system_msg = "You are a helpful assistant providing general conversation and mental health support."
    messages.append({"role": "system", "content": system_msg})
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("Chatbot: Take care! Remember, you are not alone.")
            break
        
        # Get mental health support if applicable
        mental_health_response = get_mental_health_support(user_input)
        if mental_health_response != "I'm here to help with mental health support. Can you please tell me more about what you're experiencing?":
            print(f"Chatbot: {mental_health_response}")
            continue
        
        # Create a chat completion with OpenAI
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        
        # Print chatbot response
        print(f"Chatbot: {reply}")

# Start the chatbot conversation
chat_with_user()
