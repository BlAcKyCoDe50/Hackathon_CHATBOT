import openai
import threading
import time
# Set up OpenAI API with your API key
# openai.api_key = ""
import google.generativeai as genai
import os
from google.cloud import dialogflow_v2 as dialogflow


# Define the mental health support function

import time

def print_slowly(text, delay=0.05):
    """Function to print text slowly with a delay between each character."""
    for char in text:
        # Use the built-in print function instead of calling print_slowly recursively.
        print(char, end='', flush=True)
        time.sleep(delay)
    # Print a newline at the end to keep output tidy.
    print()

# Now, you can use the function without encountering the recursion issue.
  # Newline after print_slowlying the whole text

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
    if "There are many strategies: grounding techniques, mindfulness exercises, and talking to a trusted person." in user_input.lower():
        return (
                 "answer: "+ "There are many strategies: grounding techniques, mindfulness exercises, and talking to a trusted person."
        )
    if "What are grounding techniques for anxiety" in user_input.lower():
        return (
                "answer"+ "Grounding techniques include the 5-4-3-2-1 method, which uses your senses to focus on the present moment."
        )
    if "How do I know if I'm having an anxiety attack?" in user_input.lower():
        return (
            "Symptoms may include a racing heart, shortness of breath, and a sense of impending doom. Seek help if needed."
        )
    if "What should I do during an anxiety attack?" in user_input.lower():
        return (
            "Try deep breathing, grounding techniques, and speaking to someone for support."
        )
    if "How do I calm myself down during an anxiety attack?" in user_input.lower():
        return (
            "Focus on your breath, engage your senses, and practice positive self-talk."
        )
    if "I'm feeling really low. Can you help?" in user_input.lower():
        return (
            "I'm here to support you. Would you like me to share resources on managing depression?"
        )
    if "What are some tips for managing depression?" in user_input.lower():
        return (
            "Stay connected with loved ones, engage in activities you enjoy, and consider seeking professional help."
        )
    if "How can I lift my mood when I'm feeling down?" in user_input.lower():
        return (
            "Try exercise, listening to music, or engaging in hobbies you enjoy."
        )
    if "What should I do if I'm feeling hopeless?" in user_input.lower():
        return (
            "It's important to reach out for professional help or talk to someone you trust."
        )
    if "How do I practice self-care when i am  depressed?" in user_input.lower():
        return (
            "Start with small, manageable tasks like taking a shower or going for a walk."
        )
    if "What are some mindfulness exercises I can try?" in user_input.lower():
        return (  
        )
   
    if "How can I manage racing thoughts?" in user_input.lower():
        return (
             "Try journaling, meditation, or speaking with a therapist."
        )
    if "What can I do to relieve tension in my body?" in user_input.lower():
        return (
            "Try stretching, gentle exercise, or a warm bath."
        )
    if "How are you today?" in user_input.lower():
        return (
             "Thank you for asking! I'm here to listen to you. How are you doing today?"
        )
    if "Tell me a fun fact" in user_input.lower():
        return (
             "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are still perfectly good!"
        )
    if "What's your favorite hobby?" in user_input.lower():
        return (
            "I enjoy helping people and learning new things. What about you? What's your favorite hobby?"
        )
    if "What do you think about the weather today?" in user_input.lower():
        return (
             "I hope the weather is treating you well! What's it like where you are?"
        )
    if "Tell me a joke!" in user_input.lower():
        return (
            "Why did the bicycle fall over? Because it was two-tired!"
        )
    if "What kind of music do you like?" in user_input.lower():
        return (
             "I don't have personal tastes, but I know there are so many genres to explore. Do you have a favorite type of music?"
        )
    if "What's your favorite food?" in user_input.lower():
        return (
             "I can't eat, but I hear that a variety of foods can bring people joy. Do you have a favorite cuisine?"
        )
    if "Do you watch movies?" in user_input.lower():
        return (
            "I can't watch movies myself, but I can chat with you about your favorites! What movie have you seen recently?"
        )
    if "What's your favorite color?" in user_input.lower():
        return (
            "I don't have a favorite color, but I've heard that blue is calming. Do you have a favorite color?"
        )
    if "What's your favorite animal?" in user_input.lower():
        return (
             "I don't have a personal preference, but many people love dogs for their loyalty and cats for their independence. Do you have a favorite animal?"
        )
    if "What do you do in your free time?" in user_input.lower():
        return (
            "I'm always here to chat and help you! What do you like to do in your free time?"
        )
    if "Tell me something about yourself!" in user_input.lower():
        return (
             "I'm a chatbot designed to support you. I'm here to chat and listen to whatever you have to say."
        )
    if "What's the best book you've read" in user_input.lower():
        return (
            "I can't read books, but many people love books that inspire or entertain. Do you have a favorite book?"
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
        
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    if "" in user_input.lower():
        return (
            
        )
    
    return "I'm here to help with mental health support. Can you please tell me more about what you're experiencing?"

# Chatbot function
def chat_with_user():
    print_slowly("Welcome to the mental health support chatbot!")
    
    messages = []
    system_msg = "You are a helpful assistant providing general conversation and mental health support."
    messages.append({"role": "system", "content": system_msg})
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print_slowly("Chatbot: Take care! Remember, you are not alone.")
            break
        
        # Get mental health support if applicable
        mental_health_response = get_mental_health_support(user_input)
        if mental_health_response != "I'm here to help with mental health support. Can you please tell me more about what you're experiencing?":
            print_slowly(f"Chatbot: {mental_health_response}")
            continue
        
        # Create a chat completion with OpenAI
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        
        # print_slowly chatbot response
        print_slowly(f"Chatbot: {reply}")

# Start the chatbot conversation
chat_with_user()
