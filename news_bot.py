import os
import feedparser
import smtplib
from email.message import EmailMessage

EMAIL = "evanpauljacob27@gmail.com"
APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

feeds = [
    ("BBC", "http://feeds.bbci.co.uk/news/rss.xml"),
    ("CNN", "http://rss.cnn.com/rss/edition.rss"),
    ("The Hindu", "https://www.thehindu.com/news/feeder/default.rss")
]

html = """
<h1>📰 Daily News Digest</h1>
"""

for source, url in feeds:

    feed = feedparser.parse(url)

    html += f"<h2>{source}</h2><ul>"

    for item in feed.entries[:3]:

        published = getattr(item, "published", "N/A")

        html += f"""
        <li>
            <a href="{item.link}">
                {item.title}
            </a>
            <br>
            <small>{published}</small>
        </li>
        """

    html += "</ul>"

msg = EmailMessage()

msg["Subject"] = "Daily News Digest"
msg["From"] = EMAIL
msg["To"] = EMAIL

msg.add_alternative(html, subtype="html")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, APP_PASSWORD)
    smtp.send_message(msg)

print("News email sent!")