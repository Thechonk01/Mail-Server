import logging
from email.message import EmailMessage

# Configure logging
logging.basicConfig(
    filename='logs/mailserver.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_email(envelope):
    mail_from = envelope.mail_from
    rcpt_tos = envelope.rcpt_tos
    content = envelope.content.decode('utf-8', errors='replace')
    
    logging.info(f'Email received from: {mail_from}')
    logging.info(f'Email received for: {rcpt_tos}')
    logging.info(f'Email content:\n{content}')
    
    print('Email logged successfully.')
