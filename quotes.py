from tkinter import *
import requests,json,traceback,feedparser
from PIL import Image, ImageTk
import random

medText = 28


class Quotes(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.quoteContainer = Frame(self, bg="black")
        self.quoteContainer.pack(side=TOP)
        self.quoteLbl = Label(self, text="", font=('Helvetica', medText), fg="white", bg="black")
        self.quoteLbl.pack(side=TOP, anchor=W)
        self.get_quote()

    # Picks a random quote from quotes.txt and displays, Gets changed every 5000ms #
    def get_quote(self):
        line = random.choice(open('quotes.txt', 'r', encoding='utf-8').readlines())
        self.quoteLbl.config(text=line)
        self.after(5000, self.get_quote)
