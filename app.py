from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from datetime import date
import process_data

import check

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe', options=chrome_options)
#driver = webdriver.Chrome('C:/Users/archi/chromedriver/chromedriver.exe')
driver.get('https://www.dmart.in/')
time.sleep(0.5)
#Edit this only!!!
urls = [ "https://www.dmart.in/category/dmart-grocery-aesc-dmartgrocerycore", "https://www.dmart.in/category/grocery-aesc-grocerycore", "https://www.dmart.in/category/dairy---beverages-aesc-dairyandbeveragescore","https://www.dmart.in/category/packaged-food-aesc-packagedfoodcore", "https://www.dmart.in/category/fruits---vegetables-aesc-fruitsandvegetablescore"]
headings = [ "DMart Grocery", "Grocery", "Dairy & Beverages", "Packaged Food", "Fruits & Vegetables"]
# function for ...converting the quantity and price in term of kg and price (in kg)
#Don't Touch!!
l=len(urls)
category=[]
names=[]
quantity=[]
price=[]
website=[]
city=[]
status = []
ahref_tags=[]
updated_mrp_per_kg = []
updated_quantity_per_kg = []
for i in range(l):
    time.sleep(1.5)
    count=0
    u = urls[i]
    b = headings[i]
    c = 'DMart'
    d = "Mumbai"
    #print(b)
    #Select a particular url
    driver.get(u)
    prices = []
    #Scroll to the end of the page
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(5)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
    
    
    #Start of Scraping
    item_names = driver.find_elements_by_class_name('src-client-components-product-card-vertical-card-__vertical-card-module___title')
    price = driver.find_elements_by_class_name('src-client-components-product-card-vertical-card-__vertical-card-module___amount')
    ahref_tag = driver.find_elements_by_class_name('src-client-components-product-card-vertical-card-__vertical-card-module___section-top')
    
    #Offline Start
    item_names = [item.text for item in item_names]
    index = 1
    for j in item_names:
        count+=1
        tmp = j.split(' : ')
        if len(tmp)<2:
            tmp.append('NaN')
        tmp[0],stat = process_data.comparing_ingredient_cleaning_dict(tmp[0])
        names.append(tmp[0])
        #tmp[1]=converstion(tmp[1],j)
        quantity.append(tmp[1])
        status.append(stat)
        print(tmp[0],stat)
        prices.append(price[index].text)
        u_price,u_weight =check.converstion(tmp[1],price[index].text)
        updated_mrp_per_kg.append(u_price)
        updated_quantity_per_kg.append(u_weight)
        index +=3
  
    #prices = [prices.text for prices in price]
    apn=1
    k=0
    for j in prices:
        if(k==apn):
            price.append(j)
            apn+=3
        k+=1
    for j in range(count):
        website.append(c)
        city.append(d)
        category.append(b)
        #print(j)
        #print(b)
    
    
    for i in ahref_tag:
        j = i.find_element_by_css_selector('a').get_attribute('href')
        res = j.split('/') 
        ahref_tags.append(res[-1])
    time.sleep(0.5) 


print()

# terminates the application
driver.quit()



price_date = str(date.today())
col = pd.DataFrame(list(zip( category, names, updated_quantity_per_kg, updated_mrp_per_kg)), columns =[ 'Category','Item Name','Quantity', price_date]) 
name_of_output = price_date+'_Final_Output_DMart_ID.csv'
#col.sort_values('ID')





col.to_csv(name_of_output, index = False)

#len(pd.unique(col['ID'])) 
#len(pd.unique(col['Item Name']))


 