from sheet import sheet_to_dict
from auth import autho
from create_email import create_mail
from create_email_with_attachments import create_message_with_attachment
from send_email import send_mail
from googleapiclient.discovery import build

def send(myLink,mySybject,myContent):
    service = build('gmail', 'v1', credentials=autho())
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    dic = sheet_to_dict(myLink)
    i = 0
    if dic['Email'] != None:
        for email in dic['Email'] :
            if(email!=None): 
                message = create_message_with_attachment('',email,mySybject,myContent)
                send_mail(service,'me',message)
        return 1
    return 0