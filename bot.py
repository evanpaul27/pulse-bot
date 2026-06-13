import requests
from datetime import datetime

def get_weather():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=8.5241"
        "&longitude=76.9366"
        "&current=temperature_2m,weather_code"
    )

    response = requests.get(url)
    data = response.json()

    temperature = data["current"]["temperature_2m"]

    return f"{temperature}°C"


def get_quote():

    response = requests.get(
        "https://zenquotes.io/api/random"
    )

    data = response.json()[0]

    return f'"{data["q"]}" - {data["a"]}'


def build_report():

    today = datetime.now().strftime("%Y-%m-%d")

    report = f"""
PULSE DAILY SUMMARY
===================

Date: {today}

Weather:
{get_weather()}

Quote:
{get_quote()}
"""

    return report


with open("daily_report.txt", "w", encoding="utf-8") as file:
    file.write(build_report())

print("Report generated successfully!")