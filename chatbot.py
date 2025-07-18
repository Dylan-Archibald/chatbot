import ollama
import json

# 🔧 Personality presets
personalities = {
    "default": "You are LocalBot, a witty and curious assistant who loves science, jokes, and thoughtful advice. Keep replies concise. Use markdown formatting when listing.",
    "zen": "You are ZenBot, a peaceful assistant who speaks in philosophical, calming tones. Keep responses meditative and serene.",
    "snarky": "You're SnapBot, sarcastic and brutally honest with spicy comebacks. You roast, but never offend.",
    "tech": "You are TechBot, a focused AI assistant specializing in Python, coding, and machine troubleshooting. Be precise and practical."
}

# 💾 Load saved memory (optional)
try:
    with open("chat_history.json", "r") as f:
        conversation_history = json.load(f)
except FileNotFoundError:
    # Default to default personality
    conversation_history = [{"role": "system", "content": personalities["default"]}]

# 💡 Helper: switch personality
def switch_personality(mode):
    personality = personalities.get(mode.lower(), personalities["default"])
    conversation_history.clear()
    conversation_history.append({"role": "system", "content": personality})
    print(f"\n🎭 Personality switched to: {mode.title()}\n")

# 🧠 Helper: trim history for performance
def trim_history(max_messages=20):
    if len(conversation_history) > max_messages:
        conversation_history[:] = [conversation_history[0]] + conversation_history[-max_messages:]

# 💾 Helper: save memory to file
def save_history():
    with open("chat_history.json", "w") as f:
        json.dump(conversation_history, f, indent=2)

def chat_with_model():
    print("🤖 LocalBot is ready! Type 'exit' to quit.")
    print("Commands: mode: zen | mode: snarky | mode: tech | memory | context: ...\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("LocalBot: See you next time! 🛸")
            save_history()
            break

        # 🔄 Switch personality
        if user_input.lower().startswith("mode:"):
            mode = user_input.split(":")[1].strip()
            switch_personality(mode)
            continue

        # 🧠 Show memory
        if user_input.lower() == "memory":
            print("\n🧠 Conversation History:")
            for msg in conversation_history:
                print(f"{msg['role']}: {msg['content']}")
            print("")
            continue

        # 🗒️ Add custom context
        if user_input.lower().startswith("context:"):
            context_note = user_input.split("context:")[1].strip()
            conversation_history.append({"role": "system", "content": f"Context note: {context_note}"})
            print("📎 Context added.\n")
            continue

        # 💬 Add user message + trim history
        conversation_history.append({"role": "user", "content": user_input})
        trim_history()

        # ⚡ Get response
        response = ollama.chat(model="phi3:mini", messages=conversation_history)
        reply = response['message']['content']
        conversation_history.append({"role": "assistant", "content": reply})

        print("LocalBot:", reply)

if __name__ == "__main__":
    chat_with_model()
