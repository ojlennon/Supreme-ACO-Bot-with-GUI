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
from config import ProductDetails, UserDetails, PaymentDetails, ChromeOptions

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


driver = webdriver.Chrome(options=options, executable_path= ChromeOptions.CHROME_DRIVER_PATH) #classify chrome driver and location
wait = WebDriverWait(driver, 10)
session = requests.Session()

def find_item(name):
    url = "https://www.supremenewyork.com/mobile_stock.json" #draw url 
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
        f'document.getElementById("order_billing_name").value = "{UserDetails.name}";'
        f'document.getElementById("order_email").value = "{UserDetails.email}";'
        f'document.getElementById("order_tel").value = "{UserDetails.tele}";'
        f'document.getElementById("order_billing_address").value = "{UserDetails.adr}";'
        f'document.getElementById("order_billing_zip").value = "{UserDetails.zip}";'
        f'document.getElementById("order_billing_city").value = "{UserDetails.city}";'
        f'document.getElementById("credit_card_number").value = "{PaymentDetails.cardNum}";'
        f'document.getElementById("credit_card_verification_value").value = "{PaymentDetails.cvv}";'     
    )
    
    state = Select(driver.find_element_by_id('order_billing_state'))
    state.select_by_visible_text(str(UserDetails.state))
    
    card_month = Select(driver.find_element_by_id('credit_card_month'))
    card_month.select_by_value(str(PaymentDetails.month))
    
    card_year = Select(driver.find_element_by_id('credit_card_year'))
    card_year.select_by_value(str(PaymentDetails.year))
    
    driver.find_element_by_id('order_terms').click()

    driver.find_element_by_id('submit_button').click()

if __name__ == '__main__':
    t1 = time.time()
    item_id = find_item(ProductDetails.keywords)
    colour_id = get_colour(item_id, ProductDetails.colour, ProductDetails.size)
    get_product(item_id, colour_id, ProductDetails.size)
    time.sleep(0.8)
    checkout()
    t0 = time.time()
    print('TIME: ', t0 - t1)
    print('success!')