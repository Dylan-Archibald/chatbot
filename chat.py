from ollama import chat

def run_chat(model, style, messages):
    system_msg = {"role": "system", "content": get_personality(style)}
    full_history = [system_msg] + messages
    response = chat(model=model, messages=full_history)
    return response.message.content

def get_personality(style="helpful"):
    personalities = {
        "helpful": "You are a helpful assistant.",
        "funny": "You are a witty assistant who likes to joke around.",
        "serious": "You are a no-nonsense, concise assistant."
    }
    return personalities.get(style.lower(), personalities["helpful"])

def preview_response(prompt, models=["phi3"], styles=["helpful", "funny", "serious"]):
    messages = [{"role": "user", "content": prompt}]
    for model in models:
        for style in styles:
            print(f"👤 Model: {model} | Personality: {style}")
            reply = run_chat(model, style, messages)
            print(f"💬 {reply}\n")













