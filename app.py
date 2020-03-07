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
    if dic['Email'] != None:
        for email in dic['Email'] :
            if(email!=None): 
                message = create_mail('',email,mySybject,myContent)
                send_mail(service,'me',message)
    return 'done'
eel.init('web')
eel.start('index.html', size=(700,700))