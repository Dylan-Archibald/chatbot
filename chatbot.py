import ollama

# Initial system prompt with default personality
conversation_history = [
    {"role": "system", "content": "You are LocalBot, a witty and curious assistant who loves science, jokes, and thoughtful advice."}
]

def switch_personality(mode):
    personalities = {
        "default": "You are LocalBot, a witty and curious assistant who loves science, jokes, and thoughtful advice.",
        "zen": "You are ZenBot, a peaceful assistant who speaks in calming, philosophical tones.",
        "snarky": "You're SnapBot, sarcastic and brutally honest with spicy comebacks.",
        "tech": "You are TechBot, a focused AI assistant specializing in Python, coding, and machine troubleshooting."
    }
    personality = personalities.get(mode.lower(), personalities["default"])
    # Clear history and reinit with new system prompt
    conversation_history.clear()
    conversation_history.append({"role": "system", "content": personality})
    print(f"\n🧬 Personality switched to: {mode.title()}\n")

def chat_with_model():
    print("🤖 LocalBot is ready! Type 'exit' to quit.")
    print("Type 'mode: zen', 'mode: snarky', or 'mode: tech' to switch personality.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("LocalBot: Catch you next time! 🛸")
            break

        # Handle personality switching
        if user_input.lower().startswith("mode:"):
            mode_name = user_input.split(":")[1].strip()
            switch_personality(mode_name)
            continue

        # Print memory on demand
        if user_input.lower() == "memory":
            print("\n🧠 Conversation History:")
            for msg in conversation_history:
                print(f"{msg['role']}: {msg['content']}")
            print("")
            continue

        # Add new user message
        conversation_history.append({"role": "user", "content": user_input})

        # Get response
        response = ollama.chat(model="phi3:mini", messages=conversation_history)

        reply = response['message']['content']
        conversation_history.append({"role": "assistant", "content": reply})

        print("LocalBot:", reply)

if __name__ == "__main__":
    chat_with_model()
