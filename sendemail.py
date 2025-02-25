import smtplib
import getpass
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email():
    sender_email = "gedelajhansi22@ifheindia.org"
    password = getpass.getpass("Enter App Password: ")  # Use an App Password instead of your real password
    recipient_email = "jhansi6edc99@gmail.com"
    
    # Create Email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Welcome to AI Mafia 🚀"

    # HTML Content
    html_content = r"""\
    <html>
      <body>
        <h2 style="color:blue;">Hello Everyone! 🎉</h2>
        <p>We are pleased to inform you that you have been <b>selected</b> exceptionally for your amazing abilities.</p>
        <p>Check out our website: <a href='https://example.com'>Visit Here</a></p>
        <img src="C:\Users\jhans\Downloads\Discover Easy Watercolor Art ideas.jpeg" width="300" height="200">
        <p>Thank You! 😊</p>
      </body>
    </html>
    """
    
    msg.attach(MIMEText(html_content, "html"))

    # Add Attachments (Modify with your file paths)
    file_paths = [r"C:\Users\jhans\OneDrive\Desktop\GATE _CS_2025_Syllabus.pdf"]  # List of files to attach

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
    server.login(sender_email, password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

    print("✅ HTML Email with Attachments Sent Successfully!")

send_email()
