from tkinter import *
import requests,json,traceback,feedparser
from PIL import Image, ImageTk

# Used for simple Labels #
class Splash(Frame):
    def __init__(self, parent, event_name="", fontsize="", *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = event_name # 'News' is more internationally generic
        self.newsLbl = Label(self, text=self.title, font=('Helvetica', fontsize), fg="white", bg="black")
        self.newsLbl.pack(side=TOP, anchor=W)