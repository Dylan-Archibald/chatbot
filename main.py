from chat_utils import run_chat, get_personality
import os

# 🧠 Chat history for memory tracking
chat_history = []

def add_message(role, content):
    chat_history.append({"role": role, "content": content})

# 🌟 Personality selection
personality = get_personality("funny")
add_message("system", personality)

# 💬 User initiates conversation
add_message("user", "Hello! What's your name?")

# 🚀 Run the chat and show response
response = run_chat("phi3", chat_history)
add_message("assistant", response)

print("Assistant:", response)

# 📍 Show working directory (optional)
print("Current Directory:", os.getcwd())
