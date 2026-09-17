# K-Tech Israel - AI Customer Service Bot 🤖📱

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![Gemini](https://img.shields.io/badge/Google%20Gemini-3.5%20Flash%20Lite-orange.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-AI%20Agents-blueviolet.svg)
![WhatsApp API](https://img.shields.io/badge/WhatsApp-Cloud%20API-25D366.svg)

מערכת שירות לקוחות אוטומטית וחכמה (AI Agent) עבור חברת **איי.קייטק אינטרנשיונל בע"מ** (יבואנית מכונות גילוח ותספורת). 
המערכת מנהלת פניות של לקוחות דרך **WhatsApp** ו-**SMS** במקביל, על גבי אותו מספר טלפון (055), תוך שימוש במודל שפה מתקדם של Google וניהול מצבי שיחה דרך LangGraph.

---

## ✨ תכונות מרכזיות (Key Features)

* **תמיכה מרובת ערוצים (Omnichannel):** קבלת ושליחת הודעות מול WhatsApp Cloud API של Meta, ומול רשת ה-SMS הסלולרית באמצעות טלפון פיזי משמש כ-Gateway.
* **הסלמה חכמה למנהל (Human Escalation):** זיהוי כעס, תסכול או בקשה מפורשת לנציג, והעברת השיחה בצורה חלקה ל-WhatsApp האישי של מנהל המעבדה תוך כדי עדכון הלקוח.
* **מניעת כפילויות (Idempotency Lock):** מנגנון נעילה אסינכרוני (`asyncio.Lock`) וזיכרון מטמון למניעת עיבוד כפול של הודעות SMS עקב ניסיונות חוזרים (Retries) מרשתות סלולר.
* **ניהול זיכרון אקטיבי:** סיכום אוטומטי של היסטוריית שיחות ארוכות (Memory limit optimization) למניעת עומס טוקנים על מודל ה-AI.
* **אבטחה ותשתית:** חיבור מאובטח בין שרת הענן למכשיר הסלולר הפיזי באמצעות רשת VPN פרטית של **Tailscale**.

---

## 🏗️ ארכיטקטורה וטכנולוגיות (Tech Stack)

* **Back-end:** Python, FastAPI, Uvicorn.
* **AI & NLP:** Google GenAI (Gemini 3.5 Flash Lite), LangGraph.
* **Infrastructure:** Oracle Cloud Infrastructure (OCI).
* **SMS Gateway:** מכשיר Android ייעודי (Redmi Note 9) המריץ `SmsForwarder` כשרת HTTP מקומי.
* **Networking:** Tailscale VPN לתקשורת פנימית מוצפנת, Nginx כ-Reverse Proxy.

---

## 📂 מבנה הפרויקט (Project Structure)

```text
ktech-whatsapp-bot/
├── controllers/          # ניתוב בקשות ה-Webhooks (וואטסאפ ו-SMS)
├── services/             # הלוגיקה העסקית (ai_service, sms_service, whatsapp_service)
├── tools/                # כלים עבור סוכן ה-AI (escalation_tool, business_hours_tool)
├── dtos/                 # מבני נתונים (Data Transfer Objects) לאובייקטי התקשורת
├── script/               # סקריפטים תשתיתיים (רישום Webhooks, טסטים ל-JSON)
├── db/                   # קבצי ידע סטטיים (biz_info.txt המכיל את נהלי החברה)
├── main.py               # נקודת הכניסה של אפליקציית ה-FastAPI
├── requirements.txt      # תלויות פייתון
└── .env                  # משתני סביבה (סודות וטוקנים)