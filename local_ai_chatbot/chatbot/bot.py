"""Core chatbot response logic with local JSON memory."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parents[1]
MEMORY_DIR = BASE_DIR / "data" / "memory"
TASKS_FILE = MEMORY_DIR / "tasks.json"
NOTES_FILE = MEMORY_DIR / "notes.json"
REMINDERS_FILE = MEMORY_DIR / "reminders.json"

STATIC_RESPONSES = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm running locally and working well.",
    "your name": "I am your Local AI Assistant.",
    "bye": "Goodbye!",
}


def _load_list(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig") as file:
        data = json.load(file)
    if isinstance(data, list):
        return data
    return []


def _save_list(path: Path, data: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def _next_id(prefix: str, existing_ids: list[str]) -> str:
    max_num = 0
    for item_id in existing_ids:
        if item_id.startswith(f"{prefix}-"):
            suffix = item_id.split("-", 1)[1]
            if suffix.isdigit():
                max_num = max(max_num, int(suffix))
    return f"{prefix}-{max_num + 1:03d}"


def _cmd_help() -> str:
    return (
        "Commands: hello | hi | how are you | your name | "
        "list tasks | add task <title> | done task <id> | "
        "list notes | add note <text> | "
        "list reminders | add reminder <title> at <YYYY-MM-DD HH:MM> | "
        "exit"
    )


def _list_tasks() -> str:
    tasks = _load_list(TASKS_FILE)
    if not tasks:
        return "No tasks found."
    lines = ["Tasks:"]
    for task in tasks:
        lines.append(
            f"{task.get('id', 'task-???')} | {task.get('status', 'todo')} | "
            f"{task.get('title', '')} | due {task.get('due_date', '-')}"
        )
    return "\n".join(lines)


def _add_task(raw: str) -> str:
    title = raw.strip()
    if not title:
        return "Usage: add task <title>"
    tasks = _load_list(TASKS_FILE)
    next_task_id = _next_id("task", [task.get("id", "") for task in tasks])
    new_task = {
        "id": next_task_id,
        "title": title,
        "priority": "medium",
        "due_date": datetime.now().date().isoformat(),
        "status": "todo",
        "tags": ["personal"],
    }
    tasks.append(new_task)
    _save_list(TASKS_FILE, tasks)
    return f"Task added: {next_task_id} - {title}"


def _done_task(raw: str) -> str:
    task_id = raw.strip().lower()
    if not task_id:
        return "Usage: done task <task-id>"
    tasks = _load_list(TASKS_FILE)
    for task in tasks:
        if str(task.get("id", "")).lower() == task_id:
            task["status"] = "done"
            _save_list(TASKS_FILE, tasks)
            return f"Task marked done: {task.get('id')}."
    return f"Task not found: {task_id}"


def _list_notes() -> str:
    notes = _load_list(NOTES_FILE)
    if not notes:
        return "No notes found."
    lines = ["Notes:"]
    for note in notes[-5:]:
        lines.append(f"{note.get('id', 'note-???')}: {note.get('text', '')}")
    return "\n".join(lines)


def _add_note(raw: str) -> str:
    text = raw.strip()
    if not text:
        return "Usage: add note <text>"
    notes = _load_list(NOTES_FILE)
    next_note_id = _next_id("note", [note.get("id", "") for note in notes])
    now_iso = datetime.now().astimezone().isoformat(timespec="seconds")
    notes.append(
        {
            "id": next_note_id,
            "created_at": now_iso,
            "text": text,
            "tags": ["personal"],
        }
    )
    _save_list(NOTES_FILE, notes)
    return f"Note saved: {next_note_id}"


def _list_reminders() -> str:
    reminders = _load_list(REMINDERS_FILE)
    if not reminders:
        return "No reminders found."
    lines = ["Reminders:"]
    for reminder in reminders:
        lines.append(
            f"{reminder.get('id', 'rem-???')} | {reminder.get('status', 'pending')} | "
            f"{reminder.get('title', '')} | at {reminder.get('trigger_at', '-')}"
        )
    return "\n".join(lines)


def _add_reminder(raw: str) -> str:
    if " at " not in raw:
        return "Usage: add reminder <title> at <YYYY-MM-DD HH:MM>"
    title, at_value = raw.rsplit(" at ", 1)
    title = title.strip()
    at_value = at_value.strip()
    if not title or not at_value:
        return "Usage: add reminder <title> at <YYYY-MM-DD HH:MM>"
    try:
        parsed = datetime.strptime(at_value, "%Y-%m-%d %H:%M")
    except ValueError:
        return "Invalid date format. Use: YYYY-MM-DD HH:MM"

    reminders = _load_list(REMINDERS_FILE)
    next_rem_id = _next_id("rem", [item.get("id", "") for item in reminders])
    reminders.append(
        {
            "id": next_rem_id,
            "title": title,
            "trigger_at": parsed.astimezone().isoformat(timespec="seconds"),
            "channel": "in_app",
            "status": "pending",
        }
    )
    _save_list(REMINDERS_FILE, reminders)
    return f"Reminder added: {next_rem_id} at {parsed.strftime('%Y-%m-%d %H:%M')}"


def get_response(user_message: str) -> str:
    """Return a response for a user message."""
    message = user_message.strip()
    lowered = message.lower()

    if not lowered:
        return "Please type something."

    if lowered == "help":
        return _cmd_help()

    if lowered in STATIC_RESPONSES:
        return STATIC_RESPONSES[lowered]

    if lowered == "list tasks":
        return _list_tasks()
    if lowered.startswith("add task "):
        return _add_task(message[9:])
    if lowered.startswith("done task "):
        return _done_task(message[10:])

    if lowered == "list notes":
        return _list_notes()
    if lowered.startswith("add note "):
        return _add_note(message[9:])

    if lowered == "list reminders":
        return _list_reminders()
    if lowered.startswith("add reminder "):
        return _add_reminder(message[13:])

    return "I don't understand that yet. Type 'help' for commands."
