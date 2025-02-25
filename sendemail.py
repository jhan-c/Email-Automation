import smtplib
import os
import getpass
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

if not SENDER_EMAIL or not RECIPIENT_EMAIL:
    print("Error: Missing email credentials. Please set them in the .env file.")
    exit()

def send_email():
    password = getpass.getpass("Enter App Password: ")  # Entering App Password

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = "Welcome to AI Mafia 🚀"

    # HTML Content
    html_content = """\
    <html>
      <body>
        <h2 style="color:blue;">Hello Everyone! 🎉</h2>
        <p>We are pleased to inform you that you have been <b>selected</b> exceptionally for your amazing abilities.</p>
        <p>Check out our website: <a href='https://example.com'>Visit Here</a></p>
        <p>Thank You! 😊</p>
      </body>
    </html>
    """
    
    msg.attach(MIMEText(html_content, "html"))

    # Add Attachments (Modify with your file paths)
    file_paths = ["GATE _CS_2025_Syllabus.pdf"]  # Relative paths to attachments

    for file_path in file_paths:
        if os.path.exists(file_path):  # Ensure file exists
            with open(file_path, "rb") as attachment:
                part = MIMEApplication(attachment.read(), Name=os.path.basename(file_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
                msg.attach(part)
        else:
            print(f"⚠️ File not found: {file_path}")

    # SMTP Server Setup
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  
    server.login(SENDER_EMAIL, password)
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
    server.quit()

    print("✅ HTML Email with Attachments Sent Successfully!")

send_email()
