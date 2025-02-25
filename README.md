📧 EMAIL AUTOMATION
🔹 Overview
This project helps automate sending emails with HTML content and attachments using Python. It uses the smtplib and email libraries to format emails, attach files, and send them securely via Gmail's SMTP server.

✨ What This Project Does
Sends HTML-formatted emails (including images, links, and rich text).
Allows you to attach files like PDFs or documents.
Uses secure authentication with Gmail's SMTP server.
Lets you customize email templates.

1️⃣ Clone the Repository
2️⃣ Install Dependencies

⚙️ Setting Up Gmail SMTP
Since Gmail blocks direct sign-ins from less secure apps, you'll need to set up SMTP access properly:

Step 1: Enable 2-Step Verification
    Open Google My Account.
    Scroll down to "Signing in to Google".
    Turn on 2-Step Verification (if not already enabled).

Step 2: Generate an App Password
    In "Signing in to Google", go to App Passwords.
    Select Mail as the app and Device as your choice.
    Click Generate → Copy the 16-character password.

🔐 Important Security Notes
❌ Don't use your actual Gmail password—use the App Password.
🔒 Never hardcode credentials in the script. Use environment variables.



