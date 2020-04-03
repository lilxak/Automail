from __future__ import print_function
import pickle
import os.path
from os.path import expanduser
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import base64
from googleapiclient import errors
from sheet import sheet_to_dict
 

SCOPES = ['https://mail.google.com/']
class Gmail:
    def autho(self):
        creds = None

        home_dir = expanduser("~")
        directory = os.path.join(home_dir, '.credentials')
        if not os.path.exists(directory):
            os.makedirs(directory)
        directory = os.path.join(directory, 'token.pickl')
        if os.path.exists(directory):
            with open(directory, 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(directory, 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def create_message_with_attachment(self,sender, to, subject, message_text):
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        msg = MIMEText(message_text, 'html')
        message.attach(msg)

        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def send_mail(self,service, user_id, message):
        try:
            message = (service.users().messages().send(userId=user_id, body=message)
                       .execute())
            return 'sent'
        except errors.HttpError as error:
            print('An error occurred: %s' % error)

    def send_all_mails(self,myLink, mySybject, myContent):
        service = build('gmail', 'v1', credentials=self.autho())
        # Call the Gmail API
        service.users().labels().list(userId='me').execute()
        dic = sheet_to_dict(myLink)
        if dic['Email'] != None:
            for email in dic['Email']:
                message = self.create_message_with_attachment('', email, mySybject, myContent)
                self.send_mail(service, 'me', message)
            return 1
        return 0




