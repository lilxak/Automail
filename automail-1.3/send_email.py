from googleapiclient import errors

def send_mail(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                .execute())
        return 'sent'
    except errors.HttpError as error:
        print ('An error occurred: %s' % error)