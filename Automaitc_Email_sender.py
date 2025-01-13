import os
import smtplib

def automatic_email():
    user = input("Enter Your Name  : ")
    email = input("Enter Your Email: ")
    sender_email = os.getenv("SENDER_EMAIL")  # Use environment variable for sender email
    sender_password = os.getenv("SENDER_PASSWORD")  # Use environment variable for sender password

    if not sender_email or not sender_password:
        print("Sender email and password are not set in environment variables.")
        return

    subject = "Welcome Email"
    body = f"Dear {user},\n\nWelcome to krishnas platform.\n\nBest regards,\nThe krishna creation"
    message = f"Subject: {subject}\n\n{body}"

    try:
        # Connect to Gmail SMTP server !
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message)
            print("Email Sent!")
    except Exception as e:
        print(f"An error occurred: {e}")

automatic_email()
