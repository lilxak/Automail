import eel,re
from send import send

@eel.expose # Expose this function to Javascript
def sendMailPy(myLink,mySybject,myContent):
    return send(myLink,mySybject,myContent)

eel.init('web')
eel.start('index.html', size=(800,700))