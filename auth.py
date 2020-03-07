from __future__ import print_function
import pickle
import os.path
from os.path import expanduser
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://mail.google.com/']

def autho() :
    creds = None

    home_dir = expanduser("~")
    directory = os.path.join(home_dir, '.credentials')
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = os.path.join(directory,'token.pickl')
    print('this th path' + directory)
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
