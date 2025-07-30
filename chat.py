from ollama import chat

def run_chat(model, messages):
    response = chat(model=model, messages=messages)
    return response.message.content

def get_personality(style="helpful"):
    personalities = {
        "helpful": "You are a helpful assistant.",
        "funny": "You are a witty assistant who likes to joke around.",
        "serious": "You are a no-nonsense, concise assistant."
    }
    return personalities.get(style, personalities["helpful"])
