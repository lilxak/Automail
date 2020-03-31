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

eel.init('web')
eel.start('index.html', size=(800,700))