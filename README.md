# Local Ai Chatbot

A simple local command-line chatbot project in Python.

## Quick Start

1. Create and activate a virtual environment:
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the chatbot:
   ```powershell
   python Local_Ai.py
   ```

## Project Structure

- `Local_Ai.py` - entry point
- `local_ai_chatbot/chatbot/bot.py` - chatbot logic
- `local_ai_chatbot/chatbot/main.py` - CLI loop
- `local_ai_chatbot/data/profile.json` - personal preferences and schedule
- `local_ai_chatbot/data/memory/tasks.json` - task list
- `local_ai_chatbot/data/memory/reminders.json` - reminder queue
- `local_ai_chatbot/data/memory/notes.json` - quick notes
- `local_ai_chatbot/data/memory/journal.json` - daily journal entries
- `local_ai_chatbot/data/nlu/intents.json` - sample intent training phrases
- `local_ai_chatbot/data/seeds/routines.json` - reusable routines
- `local_ai_chatbot/data/seeds/faq.json` - personal FAQ knowledge

## Commands

- `help` - show supported commands
- `list tasks` - show tasks from `data/memory/tasks.json`
- `add task <title>` - create a new task
- `done task <task-id>` - mark task as done
- `list notes` - show recent notes
- `add note <text>` - save a note
- `list reminders` - show reminders
- `add reminder <title> at <YYYY-MM-DD HH:MM>` - create reminder
- `exit` - quit chatbot

## Sample Personal File Tree

```text
ChatBot_Py/
|-- Local_Ai.py
|-- README.md
|-- requirements.txt
|-- local_ai_chatbot/
|   |-- chatbot/
|   |   |-- __init__.py
|   |   |-- bot.py
|   |   `-- main.py
|   `-- data/
|       |-- profile.json
|       |-- memory/
|       |   |-- tasks.json
|       |   |-- reminders.json
|       |   |-- notes.json
|       |   `-- journal.json
|       |-- nlu/
|       |   `-- intents.json
|       `-- seeds/
|           |-- routines.json
|           `-- faq.json
`-- .gitignore
```

## Dataset Notes

- `profile.json`: your static details (name, timezone, work hours, style).
- `memory/*.json`: changing daily data the bot updates over time.
- `nlu/intents.json`: phrase examples to map user messages to actions.
- `seeds/*.json`: starter knowledge that can be loaded on first run.

All sample data is local-only and safe to customize for personal use.
