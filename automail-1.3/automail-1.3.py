import eel,re
from send import send
import fileupload
from IPython.core.display import display

from tkinter import filedialog
from tkinter import *

  

@eel.expose # Expose this function to Javascript
def sendMailPy(myLink,mySybject,myContent):
    return send(myLink,mySybject,myContent)

@eel.expose
def fileDialog():
# This is the uploader widget
    root = Tk()
    name =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
    #name = root.filename
    root.destroy()
    return name
eel.init('web')
eel.start('index.html', size=(800,700))