from tkinter import *
import os
import sys
window = Tk()
name = ""

import subprocess
 
def run_program():
    subprocess.call(["python3", "bot.py"])
 
Button(window, text='Run', command=run_program) .grid(row=40, column=20, sticky=W)


def setInfo():
    user.name = nameentry.get()
    user.email = emailentry.get()
    user.tele = teleentry.get()
    user.adr = adrentry.get()
    user.city = cityentry.get()
    user2.keywords = keywordsentry.get()
    user2.colour = colourentry.get()
    user2.size = sizeentry.get()
    user3.cardNum = cardNumentry.get()
    user3.cvv = cvventry.get()
    user3.month = monthentry.get()

class ChromeOptions:
    CHROME_DRIVER_PATH = '/Users/jasperkatalevsky/Desktop/chromedriver'

class ProductDetails:
    def __init__(self, keywords, colour, size):
        self.keywords = keywords
        self.colour = colour
        self.size = size
    

user2 = ProductDetails("", "", "")

Label(window, text='Product', background='black', fg= 'white', font='none 12 bold') .grid(row=15, column=0, sticky=W)
keywordsentry = Entry(window, width=20, bg="black")
keywordsentry.grid(row=16, column=0, sticky=W)

Label(window, text='Colour', background='black', fg= 'white', font='none 12 bold') .grid(row=17, column=0, sticky=W)
colourentry = Entry(window, width=20, bg="black")
colourentry.grid(row=18, column=0, sticky=W)

Label(window, text='Size', background='black', fg= 'white', font='none 12 bold') .grid(row=19, column=0, sticky=W)
sizeentry = Entry(window, width=20, bg="black")
sizeentry.grid(row=20, column=0, sticky=W)




class UserDetails:
    def __init__(self, name, email, tele, adr, zip, city, state):
        self.name = name
        self.email = email 
        self.tele = tele
        self.adr = adr
        self.zip = zip
        self.city = city
        self.state = state

    
user = UserDetails("", "", "", "", "", "", "")

Label(window, text='Name', background='black', fg= 'white', font='none 12 bold') .grid(row=1, column=0, sticky=W)
nameentry = Entry(window, width=20, bg="black")
nameentry.grid(row=2, column=0, sticky=W)

Label(window, text='Email', background='black', fg= 'white', font='none 12 bold') .grid(row=3, column=0, sticky=W)
emailentry = Entry(window, width=20, bg="black")
emailentry.grid(row=4, column=0, sticky=W)

Label(window, text='Telephone', background='black', fg= 'white', font='none 12 bold') .grid(row=5, column=0, sticky=W)
teleentry = Entry(window, width=20, bg="black")
teleentry.grid(row=6, column=0, sticky=W)

Label(window, text='Address', background='black', fg= 'white', font='none 12 bold') .grid(row=7, column=0, sticky=W)
adrentry = Entry(window, width=20, bg="black")
adrentry.grid(row=8, column=0, sticky=W)

Label(window, text='Zip Code', background='black', fg= 'white', font='none 12 bold') .grid(row=9, column=0, sticky=W)
zipentry = Entry(window, width=20, bg="black")
zipentry.grid(row=10, column=0, sticky=W)

Label(window, text='City', background='black', fg= 'white', font='none 12 bold') .grid(row=11, column=0, sticky=W)
cityentry = Entry(window, width=20, bg="black")
cityentry.grid(row=12, column=0, sticky=W)

Label(window, text='State (CO)', background='black', fg= 'white', font='none 12 bold') .grid(row=13, column=0, sticky=W)
zipentry = Entry(window, width=20, bg="black")
zipentry.grid(row=14, column=0, sticky=W)

class PaymentDetails():
    def __init__(self, cardNum, cvv, month, year):
        self.cardNum = cardNum
        self.cvv = cvv
        self.month = month
        self.year = year 

user3 = PaymentDetails("", "", "", "")

Label(window, text='Card Number', background='black', fg= 'white', font='none 12 bold') .grid(row=21, column=0, sticky=W)
cardNumentry = Entry(window, width=20, bg="black")
cardNumentry.grid(row=22, column=0, sticky=W)

Label(window, text='CVV', background='black', fg= 'white', font='none 12 bold') .grid(row=23, column=0, sticky=W)
cvventry = Entry(window, width=20, bg="black")
cvventry.grid(row=24, column=0, sticky=W)

Label(window, text='Month (XX/XX)', background='black', fg= 'white', font='none 12 bold') .grid(row=25, column=0, sticky=W)
monthentry = Entry(window, width=20, bg="black")
monthentry.grid(row=26, column=0, sticky=W)

Button(window, text='Submit', width=6, command = setInfo) .grid(row=40, column=0, sticky=W)
exit_button = Button(window, text="Close", command=window.destroy) .grid(row=55, column=0, sticky=W)

window.mainloop()







