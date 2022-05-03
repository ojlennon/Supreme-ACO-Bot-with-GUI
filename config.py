from tkinter import *
import os
import sys

window = Tk()
name = ""

import subprocess
import bot
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import json
import time

headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                         'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                 "Version/13.0.3 Mobile/15E148 Safari/604.1"}

prefs = {'disk-cache-size': 4096}

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options,
                          executable_path=ChromeOptions.CHROME_DRIVER_PATH)  # classify chrome driver and location
wait = WebDriverWait(driver, 10)
session = requests.Session()


def run_program():
    subprocess.call(["python3", "bot.py"])


Button(window, text='Run', command=run()).grid(row=40, column=20, sticky=W)


def setInfo():
    details.name = nameentry.get()
    details.email = emailentry.get()
    details.tele = teleentry.get()
    details.adr = adrentry.get()
    details.city = cityentry.get()
    details.keywords = keywordsentry.get()
    details.colour = colourentry.get()
    details.size = sizeentry.get()
    details.cardNum = cardNumentry.get()
    details.cvv = cvventry.get()
    details.month = monthentry.get()
    details.year = yearentry.get()


class ChromeOptions:
    CHROME_DRIVER_PATH = '/Users/jasperkatalevsky/Desktop/chromedriver'


class Details:
    def __init__(self, name, email, tele, adr, city, keywords, colour, size, cardNum, cvv, month, state, zip, year):
        self.name = name
        self.email = email
        self.tele = tele
        self.adr = adr
        self.city = city
        self.keywords = keywords
        self.colour = colour
        self.size = size
        self.cardNum = cardNum
        self.cvv = cvv
        self.month = month
        self.year = year
        self.state = state
        self.zip = zip


details = Details("", "", "", "", "", "", "", "", "", "", "", "", "", "")

Label(window, text='Product', background='black', fg='white', font='none 12 bold').grid(row=15, column=0, sticky=W)
keywordsentry = Entry(window, width=20, bg="black")
keywordsentry.grid(row=16, column=0, sticky=W)

Label(window, text='Colour', background='black', fg='white', font='none 12 bold').grid(row=17, column=0, sticky=W)
colourentry = Entry(window, width=20, bg="black")
colourentry.grid(row=18, column=0, sticky=W)

Label(window, text='Size', background='black', fg='white', font='none 12 bold').grid(row=19, column=0, sticky=W)
sizeentry = Entry(window, width=20, bg="black")
sizeentry.grid(row=20, column=0, sticky=W)


Label(window, text='Name', background='black', fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)
nameentry = Entry(window, width=20, bg="black")
nameentry.grid(row=2, column=0, sticky=W)

Label(window, text='Email', background='black', fg='white', font='none 12 bold').grid(row=3, column=0, sticky=W)
emailentry = Entry(window, width=20, bg="black")
emailentry.grid(row=4, column=0, sticky=W)

Label(window, text='Telephone', background='black', fg='white', font='none 12 bold').grid(row=5, column=0, sticky=W)
teleentry = Entry(window, width=20, bg="black")
teleentry.grid(row=6, column=0, sticky=W)

Label(window, text='Address', background='black', fg='white', font='none 12 bold').grid(row=7, column=0, sticky=W)
adrentry = Entry(window, width=20, bg="black")
adrentry.grid(row=8, column=0, sticky=W)

Label(window, text='Zip Code', background='black', fg='white', font='none 12 bold').grid(row=9, column=0, sticky=W)
zipentry = Entry(window, width=20, bg="black")
zipentry.grid(row=10, column=0, sticky=W)

Label(window, text='City', background='black', fg='white', font='none 12 bold').grid(row=11, column=0, sticky=W)
cityentry = Entry(window, width=20, bg="black")
cityentry.grid(row=12, column=0, sticky=W)

Label(window, text='State (CO)', background='black', fg='white', font='none 12 bold').grid(row=13, column=0, sticky=W)
zipentry = Entry(window, width=20, bg="black")
zipentry.grid(row=14, column=0, sticky=W)

# class details():
#     def __init__(self, cardNum, cvv, month, year):
#         self.cardNum = cardNum
#         self.cvv = cvv
#         self.month = month
#         self.year = year
#
# user3 = details("", "", "", "")

Label(window, text='Card Number', background='black', fg='white', font='none 12 bold').grid(row=21, column=0, sticky=W)
cardNumentry = Entry(window, width=20, bg="black")
cardNumentry.grid(row=22, column=0, sticky=W)

Label(window, text='CVV', background='black', fg='white', font='none 12 bold').grid(row=23, column=0, sticky=W)
cvventry = Entry(window, width=20, bg="black")
cvventry.grid(row=24, column=0, sticky=W)

Label(window, text='Month (XX/XX)', background='black', fg='white', font='none 12 bold').grid(row=25, column=0,sticky=W)
monthentry = Entry(window, width=20, bg="black")
monthentry.grid(row=26, column=0, sticky=W)

Label(window, text="Year", background='black', fg='white', font='none 12 bold').grid(row=27, column=0,sticky=W)
yearentry = Entry(window, width=20, bg="black")
yearentry.grid(row=28,column=0,stick=W)

Button(window, text='Submit', width=6, command=setInfo).grid(row=40, column=0, sticky=W)
exit_button = Button(window, text="Close", command=window.destroy).grid(row=55, column=0, sticky=W)

window.mainloop()


def find_item(name):
    url = "https://www.supremenewyork.com/mobile_stock.json"  # draw url
    html = requests.get(url=url)
    output = json.loads(html.text)

    for category in output['products_and_categories']:
        for item in output['products_and_categories'][category]:
            if name in item['name']:
                print(item['name'])
                print(item['id'])
                return item['id']


def get_colour(item_id, colour, size):
    url = f'https://www.supremenewyork.com/shop/{item_id}.json'
    html = requests.get(url=url)
    output = json.loads(html.text)
    for product_colour in output['styles']:
        if colour in product_colour['name']:
            for product_size in product_colour['sizes']:
                if size in product_size['name']:
                    return product_colour['id']
            while (True):
                pass


def get_product(product_id, product_colour_id, size):
    """
    Opens Chrome instance and adds product to card
    """

    url = 'https://www.supremenewyork.com/mobile/#products/' + str(product_id) + '/' + str(product_colour_id)

    driver.get(url)

    wait.until(EC.presence_of_element_located((By.ID, 'cart-update')))

    options = Select(driver.find_element_by_id('size-options'))
    options.select_by_visible_text(size)
    driver.find_element_by_xpath("//*[@id='cart-update']/span").click()


def checkout():
    url = 'https://www.supremenewyork.com/mobile/#checkout'

    driver.get(url)
    wait.until(EC.presence_of_all_elements_located((By.ID, 'submit_button')))

    driver.execute_script(
        f'document.getElementById("order_billing_name").value = "{details.name}";'
        f'document.getElementById("order_email").value = "{details.email}";'
        f'document.getElementById("order_tel").value = "{details.tele}";'
        f'document.getElementById("order_billing_address").value = "{details.adr}";'
        f'document.getElementById("order_billing_zip").value = "{details.zip}";'
        f'document.getElementById("order_billing_city").value = "{details.city}";'
        f'document.getElementById("credit_card_number").value = "{details.cardNum}";'
        f'document.getElementById("credit_card_verification_value").value = "{details.cvv}";'
    )

    state = Select(driver.find_element_by_id('order_billing_state'))
    state.select_by_visible_text(str(details.state))

    card_month = Select(driver.find_element_by_id('credit_card_month'))
    card_month.select_by_value(str(details.month))

    card_year = Select(driver.find_element_by_id('credit_card_year'))
    card_year.select_by_value(str(details.year))

    driver.find_element_by_id('order_terms').click()

    driver.find_element_by_id('submit_button').click()


def run():
    t1 = time.time()
    item_id = find_item(details.keywords)
    colour_id = get_colour(item_id, details.colour, details.size)
    get_product(item_id, colour_id, details.size)
    time.sleep(0.8)
    checkout()
    t0 = time.time()
    print('TIME: ', t0 - t1)
    print('success!')
