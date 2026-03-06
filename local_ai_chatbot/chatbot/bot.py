"""Core chatbot response logic."""

from __future__ import annotations


RESPONSES = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "how are you": "I'm running locally and working well.",
    "your name": "I am your Local AI Assistant.",
    "help": "Try: hello, hi, how are you, your name, exit",
    "bye": "Goodbye!",
}


def get_response(user_message: str) -> str:
    """Return a response for a user message."""
    message = user_message.strip().lower()

    if not message:
        return "Please type something."

    return RESPONSES.get(message, "I don't understand that yet.")

