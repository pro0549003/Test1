# main.py
import random
from datetime import datetime

def get_greeting(hour):
    """Return a greeting based on the current hour."""
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"


def create_greeting(name):
    now = datetime.now()
    greeting = get_greeting(now.hour)

    messages = [
        "I hope you're having an amazing day!",
        "Wishing you a fantastic day ahead!",
        "It's great to see you!",
        "May your day be filled with success and happiness!",
        "Keep smiling and keep doing great things!"
    ]

    emojis = ["😊", "🌟", "🚀", "🎉", "✨", "😎"]

    message = random.choice(messages)
    emoji = random.choice(emojis)

    print("\n" + "=" * 55)
    print("        🌈 ADVANCED GREETING SYSTEM 🌈")
    print("=" * 55)

    print(f"\n{emoji} {greeting}, {name}!")
    print(f"📅 Date: {now.strftime('%A, %B %d, %Y')}")
    print(f"⏰ Time: {now.strftime('%I:%M:%S %p')}")
    print(f"💬 {message}")

    print("\n       __________________________")
    print("      |                          |")
    print(f"      |   Hello, {name:^12}!   |")
    print("      |__________________________|")

    print("\n" + "=" * 55)


# Main program
print("🚀 Starting Greeting System...")

name = input("Enter your name: ").strip()

if not name:
    name = "Friend"

create_greeting(name)

print("\nThank you for using the Advanced Greeting System! 👋")

