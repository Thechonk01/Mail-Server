import dkim
from config import secrets, settings

def sign_email(message_bytes):
    with open(secrets.DKIM_PRIVATE_KEY_PATH, 'rb') as fh:
        dkim_private_key = fh.read()
    
    headers = [b"From", b"To", b"Subject"]
    
    signature = dkim.sign(
        message=message_bytes,
        selector=secrets.DKIM_SELECTOR.encode(),
        domain=settings.DOMAIN.encode(),
        privkey=dkim_private_key,
        include_headers=headers
    )
    
    return signature + message_bytes
