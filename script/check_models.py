import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ שגיאה: מפתח ה-API לא נמצא בקובץ .env")
    exit()

client = genai.Client(api_key=api_key)

print("="*50)
print("🔍 מבקש מגוגל את רשימת המודלים הזמינים... 🔍")
print("="*50)

try:
    models = client.models.list()
    for model in models:
        print(f"📌 שם המודל (בקוד): {model.name}")
        print(f"📖 תיאור: {model.description}")
        print("-" * 50)
except Exception as e:
    print(f"❌ שגיאה בשליפת המודלים: {e}")