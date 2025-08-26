from chat_utils import run_chat, get_personality
import os

chat_history = []

def add_message(role, content):
    chat_history.append({"role": role, "content": content})
    
personality = get_personality("funny")
add_message("system", personality)

add_message("user", "Hello! What's your name?")

response = run_chat("phi3", chat_history)
add_message("assistant", response)

print("Assistant:", response)

print("Current Directory:", os.getcwd())
