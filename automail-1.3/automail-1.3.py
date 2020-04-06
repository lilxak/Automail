import eel,re
from send import send_all_mails
import fileupload
from IPython.core.display import display
from tkinter import filedialog, Tk


@eel.expose # Expose this function to Javascript
def sendMailPy(myLink,mySybject,myContent):
    return send_all_mails(myLink,mySybject,myContent)

@eel.expose
def fileDialog():
# This is the uploader widget
    root = Tk()
    name =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
    root.destroy()
    return name

# here you return the names of eps 
@eel.expose
def getEpsFromPython(token):
    return 'yasser belhimer;zaki;sido;x;y;z;r;s;b'


@eel.expose
def sendMailExpa(selectedEps,mySybject,myContent):
    listSelectedEps = selectedEps.split(";")
    for i in range(len(listSelectedEps)):
        listSelectedEps[i] = listSelectedEps[i].split("#")
    
    print(listSelectedEps)
    return 1

eel.init('web')

try:
    eel.start('index.html', size=(800,700))
except OSError:
    try:
        eel.start('index.html', mode='firefox', size=(800,700))
    except OSError:
        eel.start('index.html', mode='edge', size=(800,700))