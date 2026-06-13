import os
import requests
import smtplib
from email.message import EmailMessage

CITY = "Thiruvananthapuram"

API_KEY = os.getenv("OPENWEATHER_API_KEY")
EMAIL = "evanpauljacob27@gmail.com"
APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={CITY}&appid={API_KEY}&units=metric"
)

data = requests.get(url).json()

temp = data["main"]["temp"]
weather = data["weather"][0]["main"]

print(f"Temperature: {temp}°C")
print(f"Weather: {weather}")

if temp > 20 or weather.lower() in ["rain", "drizzle", "thunderstorm"]:

    msg = EmailMessage()

    msg["Subject"] = "⚠ Weather Alert"
    msg["From"] = EMAIL
    msg["To"] = EMAIL

    msg.set_content(
        f"""
Weather Alert for {CITY}

Temperature: {temp}°C
Condition: {weather}

Stay prepared!
"""
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

    print("Alert email sent!")

else:
    print("No alert needed.")