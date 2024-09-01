from aiosmtpd.controller import Controller
from aiosmtpd.handlers import AsyncMessage
from email.message import EmailMessage
from .utils import log_email
from config import settings

class CustomSMTPHandler(AsyncMessage):
    async def handle_message(self, message: EmailMessage):
        # Log the email
        log_email(self.envelope)
        
        # Here you can implement additional processing, such as:
        # - Saving the email to a database
        # - Forwarding the email
        # - Triggering other actions based on email content
        
        return '250 Message accepted for delivery'

def start_smtp_server():
    handler = CustomSMTPHandler()
    controller = Controller(
        handler,
        hostname=settings.SMTP_SERVER_HOST,
        port=settings.SMTP_SERVER_PORT
    )
    controller.start()
    print(f'SMTP server started at {settings.SMTP_SERVER_HOST}:{settings.SMTP_SERVER_PORT}')
