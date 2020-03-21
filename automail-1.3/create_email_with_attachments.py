from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mimetypes

import base64
def create_message_with_attachment(sender, to, subject, message_text):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text,'html')
    message.attach(msg)

    
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}