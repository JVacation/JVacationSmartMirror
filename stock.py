from yahoo_fin import stock_info as si
from tkinter import *
import requests,json,traceback,feedparser
from PIL import Image, ImageTk
from datetime import datetime, timedelta

medText = 28
yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')


# Main Widget Frame #
class Stock(Frame):
    
    def __init__(self, parent, event_name="", *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'Stocks'
        # Packing Frame with Labels #
        self.stockLbl = Label(self, text=self.title, font=('Helvetica', medText), fg="white", bg="black")
        self.stockLbl.pack(side=TOP, anchor=N)
        self.stockContainer = Frame(self, bg="black")
        self.stockContainer.pack(side=TOP)
        self.get_stocks(event_name)

     # Calling listStocks Function #
    def get_stocks(self, event_name=""):
        self.stockList = event_name.split(",")
        for stock in self.stockList:
            stocks = listStocks(self.stockContainer, stock)
            stocks.pack(side=TOP, anchor=N)
        self.after(5000, self.get_stocks)

# Stocks Function # 
class listStocks(Frame):
    def __init__(self, parent, event_name=""):
        Frame.__init__(self, parent, bg='black')
        self.stockName = event_name
        # Assigning Icons #
        dollar = Image.open("icons/14.png")
        dollar = dollar.resize((25, 25), Image.ANTIALIAS)
        dollar = dollar.convert('RGB')
        photo = ImageTk.PhotoImage(dollar)

        upArrow = Image.open("icons/17.png")
        upArrow = upArrow.resize((25, 25), Image.ANTIALIAS)
        upArrow = upArrow.convert('RGB')
        upPhoto = ImageTk.PhotoImage(upArrow)

        downArrow = Image.open("icons/15.png")
        downArrow = downArrow.resize((25, 25), Image.ANTIALIAS)
        downArrow = downArrow.convert('RGB')
        downPhoto = ImageTk.PhotoImage(downArrow)

        evenArrow = Image.open("icons/16.png")
        evenArrow = evenArrow.resize((25, 25), Image.ANTIALIAS)
        evenArrow = evenArrow.convert('RGB')
        evenPhoto = ImageTk.PhotoImage(evenArrow)

        self.stockNameLbl = Label(self, text=self.stockName, font=('Helvetica'), fg="white", bg="black")
        self.stockNameLbl.pack(side=TOP, anchor=N)

        self.iconLbl = Label(self, bg='black', image=photo)
        self.iconLbl.image = photo
        self.iconLbl.pack(side=LEFT, anchor=W)
        
        # Getting current live price for Stock #
        self.stockQuote = si.get_live_price(self.stockName)
        # Gets Yesterday closing price for stock #
        self.stockYesterday = si.get_quote_table(self.stockName, dict_result=True)
        if self.stockQuote > self.stockYesterday['Previous Close']:
            self.eventNameLbl = Label(self, text=round(self.stockQuote, 3), font=('Helvetica'), fg="green", bg="black")
            self.arrowLbl = Label(self, bg='black', image=upPhoto)
            self.arrowLbl.image = upPhoto
        elif self.stockQuote < self.stockYesterday['Previous Close']:
            self.eventNameLbl = Label(self, text=round(self.stockQuote, 3), font=('Helvetica'), fg="red", bg="black")
            self.arrowLbl = Label(self, bg='black', image=downPhoto)
            self.arrowLbl.image = downPhoto
        else:
            self.eventNameLbl = Label(self, text=round(self.stockQuote, 3), font=('Helvetica'), fg="white", bg="black")
            self.arrowLbl = Label(self, bg='black', image=evenPhoto)
            self.arrowLbl.image = evenPhoto
        self.eventNameLbl.pack(side=LEFT, anchor=W)
        self.arrowLbl.pack(side=LEFT, anchor=W)