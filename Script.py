from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import shutil
import time
import os
import json
import re

def start_driver(headless=True):
    if not headless:
        return webdriver.Firefox()
    chrome_options = webdriver.FirefoxOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    return webdriver.Firefox()




def get_product_data(product, raw_data_file):
  
    Product = product.find("div", {"class": "src-client-components-product-card-vertical-card-__vertical-card-module___title-container"}).text
    Quantity = product.find("div", {"class": "src-client-components-form-elements-bootstrap-select-__bootstrap-select-module___option"}).text
    Price = product.find("span", {"class": "src-client-components-product-card-vertical-card-__vertical-card-module___amount"}).text

    with open(raw_data_file, "a") as f:
        data = json.dumps({
           
            'Product': Product,
            'Quantity': Quantity,
            'Price': Price,
          
        })
        f.write(data + "\n")

 


def dump_json(raw_data_file, out_data_file):
    with open(raw_data_file) as f:
        data = f.read().strip().split("\n")
    js_data = list(map(lambda x: json.loads(x), data))

    with open(out_data_file, "w") as f:
        json.dump(js_data, f, indent=2)


if __name__ == "__main__":
    driver = start_driver()

    DEBUG = True
    OUTPUT_DIR = "Output"
    out_data_file = os.path.join(OUTPUT_DIR, "data.json")
    delay = 8

    with open('links.txt', 'r') as f:
        url_list = f.read().split("\n")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    raw_data_file = os.path.join(OUTPUT_DIR, "raw_data.txt")
    with open(raw_data_file, "w") as f:
        pass

    for url in url_list:
        driver.get(url)
        print("Starting Download from: {}".format(url))

        time.sleep(delay)
        html = driver.execute_script("return document.documentElement.outerHTML")
        soup = bs(html, 'html.parser')
        products = soup.findAll("div", {"class": "src-client-components-product-card-vertical-card-__vertical-card-module___title-container"})
        rel_url = re.sub(r"/?.*", "", url)
        rel_url = rel_url.lstrip('https://www.dmart.in/')

        for product in products:
            get_product_data(product, raw_data_file)

        print("Downloaded all data from: ".format(url))

    print("Download finished from all the links.")
    dump_json(raw_data_file, out_data_file)
    print("JSON file saved as {}".format(raw_data_file))

    driver.quit()
