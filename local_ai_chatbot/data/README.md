# Data Guide

This folder stores all personal chatbot data locally.

## Files

- `profile.json`: User profile and preferences.
- `memory/tasks.json`: Task items with status and due date.
- `memory/reminders.json`: Reminder events with timestamps.
- `memory/notes.json`: Short captured notes.
- `memory/journal.json`: Daily reflections.
- `nlu/intents.json`: Intent names and example utterances.
- `seeds/routines.json`: Routine templates.
- `seeds/faq.json`: FAQ seed knowledge.

## Conventions

- Use ISO dates (`YYYY-MM-DD`) and ISO datetime (`YYYY-MM-DDTHH:mm:ss+offset`).
- Keep IDs unique (`task-001`, `note-001`, etc.).
- Prefer lowercase intent names (`add_task`, `list_tasks`).
- `memory` files are mutable at runtime; `seeds` are starter data.
