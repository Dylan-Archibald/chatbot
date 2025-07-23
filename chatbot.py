import ollama
import json
import os

# 🎭 Personality presets
PERSONALITIES = {
    "default": "You are LocalBot, a witty and curious assistant who loves science, jokes, and thoughtful advice. Keep replies concise. Use markdown formatting when listing.",
    "zen": "You are ZenBot, a peaceful assistant who speaks in philosophical, calming tones. Keep responses meditative and serene.",
    "snarky": "You're SnapBot, sarcastic and brutally honest with spicy comebacks. You roast, but never offend.",
    "tech": "You are TechBot, a focused AI assistant specializing in Python, coding, and machine troubleshooting. Be precise and practical."
}

# 📁 Memory file path
MEMORY_FILE = "chat_history.json"

# 🧠 Load memory or initialize
def load_history():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Corrupt memory file. Starting fresh.")
    return [{"role": "system", "content": PERSONALITIES["default"]}]

# 💾 Save memory
def save_history(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

# 🔄 Switch personality
def switch_personality(mode, history):
    personality = PERSONALITIES.get(mode.lower(), PERSONALITIES["default"])
    history.clear()
    history.append({"role": "system", "content": personality})
    print(f"\n🎭 Personality switched to: {mode.title()}\n")

# ✂️ Trim memory for performance
def trim_history(history, max_messages=20):
    if len(history) > max_messages:
        history[:] = [history[0]] + history[-max_messages:]

# 🧑‍💻 Chat loop
def chat_with_model():
    history = load_history()
    print("🤖 LocalBot is ready! Type 'exit' to quit.")
    print("Commands → mode: zen | mode: snarky | mode: tech | memory | context: ...\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("LocalBot: See you next time! 🛸")
            save_history(history)
            break

        if user_input.lower().startswith("mode:"):
            mode = user_input.split("mode:", 1)[1].strip()
            switch_personality(mode, history)
            continue

        if user_input.lower() == "memory":
            print("\n🧠 Conversation History:")
            for msg in history:
                print(f"{msg['role'].title()}: {msg['content']}")
            print("")
            continue

        if user_input.lower().startswith("context:"):
            context_note = user_input.split("context:", 1)[1].strip()
            history.append({"role": "system", "content": f"Context note: {context_note}"})
            print("📎 Context added.\n")
            continue

        history.append({"role": "user", "content": user_input})
        trim_history(history)

        try:
            response = ollama.chat(model="phi3:mini", messages=history)
            reply = response["message"]["content"]
        except Exception as e:
            reply = f"⚠️ Model error: {e}"

        history.append({"role": "assistant", "content": reply})
        print("LocalBot:", reply)

if __name__ == "__main__":
    chat_with_model()
