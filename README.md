# chatbot
🧠 LocalBot: Lightweight AI Chatbot with Memory and Personality
LocalBot is a modular, locally run AI chatbot built with Python and powered by the Phi-3.5 Mini model via Ollama. It supports personality switching, short-term memory, and conversational context — all in under 8 GB RAM!

🚀 Features
🧬 Short-term memory tracking across conversations

🎭 Personality switching (ZenBot, TechBot, SnapBot, etc.)

🛠️ Simple command interface (mode:, memory, context:)

💬 Natural conversations with markdown-enhanced formatting

💾 Save chat history across sessions using JSON

✅ Works locally with lightweight models (perfect for laptops!)

🛠️ Setup Instructions
Requirements
Python 3.12+

Ollama installed and added to PATH

phi3:mini model pulled via Ollama

Installation
bash
# Create virtual environment
python -m venv chatbot-env
chatbot-env\Scripts\activate

# Install dependencies
pip install ollama
Pull the model
bash
ollama pull phi3:mini
💬 Run the Chatbot
Save the script as chatbot.py, then run:

bash
python chatbot.py
✨ Commands
Command	Description
mode: tech	Switch personality to TechBot
mode: zen	Switch personality to ZenBot
memory	View current conversation memory
context: ...	Inject user-defined context into system prompt
exit	Quit the chat gracefully
📂 Project Structure
chatbot.py
chat_history.json  # (Optional) persisted memory
README.md
🧠 Model Info
Powered by Phi-3.5 Mini, a 3.8B parameter model optimized for reasoning and efficiency. Can be swapped with other models like gemma:2b, deepseek:1.5b, or smollm:1.7b.

📚 Learning Resources
🔗 Ollama Python SDK Guide

🔗 LangChain Setup Docs

🔗 Prompt Engineering Principles

🔗 Copilot Pages Guide

🤖 Future Ideas
🗂️ Persistent long-term memory with file loading

🧠 Integration with LangChain or llamaindex for document Q&A

🗣️ Voice input/output using pyttsx3 and speechrecognition

🌐 Web search integration or plugin support

