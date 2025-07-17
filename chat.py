111from ollama import chat
1111111
# Start the chat history
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello! What's your name?"}
]

# Run chat with the model
response = chat(model="phi3", messages=messages)

# Show the response
print("Assistant:", response.message.content)

import os
print(os.getcwd())
