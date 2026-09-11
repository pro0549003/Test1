import random
from datetime import datetime


# Supported languages
LANGUAGES = {
    "1": "English",
    "2": "Spanish",
    "3": "French",
    "4": "German",
    "5": "Japanese",
    "6": "Hindi",
    "7": "Chinese"
}


# Translations
TRANSLATIONS = {
    "English": {
        "morning": "Good morning",
        "afternoon": "Good afternoon",
        "evening": "Good evening",
        "night": "Good night",
        "messages": [
            "I hope you're having an amazing day!",
            "Wishing you a fantastic day ahead!",
            "It's great to see you!",
            "May your day be filled with success and happiness!",
            "Keep smiling and keep doing great things!"
        ],
        "date": "Date",
        "time": "Time",
        "message": "Message",
        "thank_you": "Thank you for using the Advanced Greeting System!"
    },

    "Spanish": {
        "morning": "Buenos días",
        "afternoon": "Buenas tardes",
        "evening": "Buenas noches",
        "night": "Buenas noches",
        "messages": [
            "¡Espero que estés teniendo un día increíble!",
            "¡Te deseo un día fantástico!",
            "¡Es genial verte!",
            "¡Que tu día esté lleno de éxito y felicidad!",
            "¡Sigue sonriendo y haciendo grandes cosas!"
        ],
        "date": "Fecha",
        "time": "Hora",
        "message": "Mensaje",
        "thank_you": "¡Gracias por usar el Sistema Avanzado de Saludos!"
    },

    "French": {
        "morning": "Bonjour",
        "afternoon": "Bon après-midi",
        "evening": "Bonsoir",
        "night": "Bonne nuit",
        "messages": [
            "J'espère que tu passes une excellente journée !",
            "Je te souhaite une journée fantastique !",
            "C'est un plaisir de te voir !",
            "Que ta journée soit remplie de succès et de bonheur !",
            "Continue de sourire et de faire de grandes choses !"
        ],
        "date": "Date",
        "time": "Heure",
        "message": "Message",
        "thank_you": "Merci d'avoir utilisé le Système Avancé de Salutations !"
    },

    "German": {
        "morning": "Guten Morgen",
        "afternoon": "Guten Tag",
        "evening": "Guten Abend",
        "night": "Gute Nacht",
        "messages": [
            "Ich hoffe, du hast einen großartigen Tag!",
            "Ich wünsche dir einen fantastischen Tag!",
            "Schön, dich zu sehen!",
            "Möge dein Tag voller Erfolg und Glück sein!",
            "Bleib lächelnd und mach weiterhin großartige Dinge!"
        ],
        "date": "Datum",
        "time": "Zeit",
        "message": "Nachricht",
        "thank_you": "Vielen Dank, dass du das Erweiterte Begrüßungssystem benutzt hast!"
    },

    "Japanese": {
        "morning": "おはようございます",
        "afternoon": "こんにちは",
        "evening": "こんばんは",
        "night": "おやすみなさい",
        "messages": [
            "素晴らしい一日をお過ごしください！",
            "今日も素敵な一日になりますように！",
            "お会いできてうれしいです！",
            "成功と幸せに満ちた一日になりますように！",
            "笑顔で素晴らしいことを続けてください！"
        ],
        "date": "日付",
        "time": "時間",
        "message": "メッセージ",
        "thank_you": "高度な挨拶システムをご利用いただき、ありがとうございます！"
    },

    "Hindi": {
        "morning": "सुप्रभात",
        "afternoon": "नमस्कार",
        "evening": "शुभ संध्या",
        "night": "शुभ रात्रि",
        "messages": [
            "मुझे उम्मीद है कि आपका दिन शानदार हो!",
            "आपका दिन बहुत अच्छा रहे!",
            "आपसे मिलकर खुशी हुई!",
            "आपका दिन सफलता और खुशियों से भरा हो!",
            "मुस्कुराते रहें और शानदार काम करते रहें!"
        ],
        "date": "तारीख",
        "time": "समय",
        "message": "संदेश",
        "thank_you": "Advanced Greeting System का उपयोग करने के लिए धन्यवाद!"
    },

    "Chinese": {
        "morning": "早上好",
        "afternoon": "下午好",
        "evening": "晚上好",
        "night": "晚安",
        "messages": [
            "希望你今天过得非常愉快！",
            "祝你今天有美好的一天！",
            "很高兴见到你！",
            "愿你的一天充满成功和幸福！",
            "保持微笑，继续做伟大的事情！"
        ],
        "date": "日期",
        "time": "时间",
        "message": "消息",
        "thank_you": "感谢您使用高级问候系统！"
    }
}


def get_greeting(hour, language):
    """Return a greeting based on the current hour and selected language."""

    translation = TRANSLATIONS[language]

    if 5 <= hour < 12:
        return translation["morning"]
    elif 12 <= hour < 17:
        return translation["afternoon"]
    elif 17 <= hour < 21:
        return translation["evening"]
    else:
        return translation["night"]


def create_greeting(name, language):
    """Create and display a greeting in the selected language."""

    now = datetime.now()
    translation = TRANSLATIONS[language]

    greeting = get_greeting(now.hour, language)

    message = random.choice(translation["messages"])

    emojis = ["😊", "🌟", "🚀", "🎉", "✨", "😎"]
    emoji = random.choice(emojis)

    print("\n" + "=" * 55)
    print("        🌈 ADVANCED GREETING SYSTEM 🌈")
    print("=" * 55)

    print(f"\n{emoji} {greeting}, {name}!")

    print(
        f"📅 {translation['date']}: "
        f"{now.strftime('%A, %B %d, %Y')}"
    )

    print(
        f"⏰ {translation['time']}: "
        f"{now.strftime('%I:%M:%S %p')}"
    )

    print(f"💬 {translation['message']}: {message}")

    print("\n       __________________________")
    print("      |                          |")
    print(f"      |   Hello, {name:^12}!   |")
    print("      |__________________________|")

    print("\n" + "=" * 55)


# Main program
print("🚀 Starting Multi-Language Greeting System...")
print("\nChoose your language:")

for number, language in LANGUAGES.items():
    print(f"{number}. {language}")

choice = input("\nEnter your choice (1-7): ").strip()

# Default to English if the choice is invalid
language = LANGUAGES.get(choice, "English")

print(f"\nSelected language: {language}")

name = input("Enter your name: ").strip()

if not name:
    name = "Friend"

create_greeting(name, language)

print(f"\n{TRANSLATIONS[language]['thank_you']} 👋")

