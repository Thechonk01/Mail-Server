import os

# Server Configuration
SMTP_SERVER_HOST = '192.168.68.129'
SMTP_SERVER_PORT = 25  # Standard SMTP port

# Logging Configuration
LOG_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs', 'mailserver.log')

# Domain Configuration
DOMAIN = 'aidanhenderson.dev'  # Replace with your domain
