import smtplib
from email.message import EmailMessage
from server.dkim_signer import sign_email
from config import settings

def send_email(sender, recipient, subject, body):
    # Create email message
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)
    
    # Convert message to bytes
    message_bytes = msg.as_bytes()
    
    # Sign the email with DKIM
    signed_message = sign_email(message_bytes)
    
    # Send email
    with smtplib.SMTP('localhost', settings.SMTP_SERVER_PORT) as server:
        server.sendmail(sender, recipient, signed_message)
        print(f'Email sent to {recipient}')

if __name__ == '__main__':
    sender = "admin@aidanhenderson.dev"
    recipient = input("Enter recipient email: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    
    send_email(sender, recipient, subject, body)
