# coding: utf-8
from tkinter import filedialog
from tkinter import *
import main
import os
import inspect

class Window(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("AudioTranslator")
        self.pack(fill=BOTH,expand=1)

        getAudio = Button(self,text="Get Audio",command=self.getFilePath)
        getAudio.place(x=225,y = 0)

        self.path = Entry(self)
        self.path.place(x=20,y=4,height = 22 , width = 200)
        
        convert = Button(self,text="Convert",command=self.createAudio)
        convert.place(x=25,y=40,width = 60)

        play = Button(self,text="Play",command=self.playTranslated)
        play.place(x=90,y=40,width = 60)

    def createAudio(self):
        self.audio = main.createAudioTrack(self.path.get())

    def playTranslated(self):
        main.textReading(self.audio)

    def getFilePath(self):
        self.set_text(filedialog.askopenfilename(initialdir = os.path.dirname(os.path.abspath(inspect.stack()[0][1])),title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg"))))
        
            
    def set_text(self,text):
        self.path.delete(0,END)
        self.path.insert(0,text)

root = Tk()
root.geometry("600x400")
app = Window(root)

root.mainloop()
