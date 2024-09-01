import os

# Path to your DKIM private key
DKIM_PRIVATE_KEY_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dkim', 'private.key')

# DKIM Selector
DKIM_SELECTOR = 'mail'  # Use the selector you chose when setting up DKIM
