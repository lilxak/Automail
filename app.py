import eel,re
from sheet import sheet_to_dict
from auth import autho
from create_email import create_mail
from send_email import send_mail
from googleapiclient.discovery import build


@eel.expose # Expose this function to Javascript
def sendMailPy(myLink,mySybject,myContent):
    service = build('gmail', 'v1', credentials=autho())
    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    dic = sheet_to_dict(myLink)
    emails = ''
    i = 0
    if dic['Email'] != None:
        for email in dic['Email'] :
            if(email!=None): 
                if(i==0):
                    emails+=email
                    i = 1
                else:
                    emails += ',' + email
        if(i==1):
            message = create_mail('',emails,mySybject,myContent)
            send_mail(service,'me',message)
    return 'done'
eel.init('web')
eel.start('index.html', size=(700,700))