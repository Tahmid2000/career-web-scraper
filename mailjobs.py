import smtplib
from secrets import *
from email.message import EmailMessage


def mailToMe(jobs):
    msg = EmailMessage()
    msg['Subject'] = 'Daily Internship Openings'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(jobs, subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
