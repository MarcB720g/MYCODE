from cgitb import html
from email.message import EmailMessage
import imp
from pydoc import HTMLDoc
import smtplib
import ssl
from email.message import EmailMessage

#things we need for an email -> subject, a recipient, a sender, a body and password. 

subject = "Email From Python"
body = "This is a test email from python"
sender_email = "mbaskin056@gmail.com"
receiver_email = "mbaskin056@gmail.com"
password = input("enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")
context = ssl.create_defeault_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")