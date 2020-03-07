from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import mimetypes

import base64

def create_mail(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
