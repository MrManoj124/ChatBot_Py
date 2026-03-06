"""Command-line runner for the Local Ai Chatbot."""

from __future__ import annotations

from .bot import get_response


def run_chatbot() -> None:
    print("Local AI Chatbot Started!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Bot: Goodbye!")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")

