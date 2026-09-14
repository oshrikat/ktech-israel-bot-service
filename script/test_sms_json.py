import requests
import time

# ה-IP של הרדמי החדש ב-Tailscale!
PHONE_API_URL = "http://100.71.143.75:5000/sms/send"

TARGET_PHONE = "0535204447" # המספר האישי שלך לקבלת ההודעה
CURRENT_TIME = int(time.time() * 1000)

payload = {
    "data": {
        "sim_slot": 1,  
        "phone_numbers": TARGET_PHONE,
        "msg_content": "בדיקת מעבדה מבודדת מ-VS Code: ה-SMS נשלח בהצלחה!"
    },
    "timestamp": CURRENT_TIME,
    "sign": ""
}

headers = {
    "Content-Type": "application/json; charset=utf-8"
}

print("="*40)
print(f"🚀 מנסה להתחבר לטלפון בכתובת: {PHONE_API_URL} ... 🚀")
try:
    response = requests.post(
        PHONE_API_URL, 
        json=payload, 
        headers=headers, 
        timeout=10
    )
    print(f"📡 סטטוס חיבור: {response.status_code}")
    print(f"📦 תשובה מהאפליקציה: {response.text}")
except Exception as e:
    print(f"❌ שגיאת התחברות: {e}")
print("="*40)