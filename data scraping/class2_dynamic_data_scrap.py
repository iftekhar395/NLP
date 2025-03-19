from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import math

driver = webdriver.Firefox()
driver.get('https://www.daraz.com.bd/mens-eyeglasses/')

#driver.maximize_window()

#image source
'''
/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img
/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/a/div/img

/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img
/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/a/div/img
//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img
'''
#text(name)
'''
//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a
//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/a
'''
#text(price)
'''
//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span
//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[3]/span
'''

data = []
#img_data = []
#/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]
total_products = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]').text
print(total_products)
pattern = r"\b\d+\b"
is_matched = re.search(pattern,total_products)
np = 0

if is_matched:
        product_count = driver.find_elements(By.CSS_SELECTOR,'div.Ms6aG')
        product_count = len(product_count)
        no_of_total_products = is_matched.group()
        np = int(no_of_total_products)
        np = math.ceil(np/product_count)
        #print(np)
for pageno in range(1,np+1):
    castPageNo = int(pageno)
    driver.get(f'https://www.daraz.com.bd/mens-eyeglasses/?page={castPageNo}')
    product_count = driver.find_elements(By.CSS_SELECTOR,'div.Ms6aG')
    product_count = len(product_count)
    #print(len(product_count), type(product_count))
    for x in range(1,product_count):
        castX = str(x)
        image_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+castX+']/div/div/div[1]/div/a/div/img'
        name_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+castX+']/div/div/div[2]/div[2]/a'
        price_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+castX+']/div/div/div[2]/div[3]/span'

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, price_xpath)))
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        product_img = driver.execute_script("return arguments[0].src;", driver.find_element(By.XPATH,image_xpath))
        #product_img = driver.find_element(By.XPATH,image_xpath).get_attribute('src')
        #img_data.append(product_img)

        product_text = driver.find_element(By.XPATH,name_xpath).text
        product_price = driver.find_element(By.XPATH,price_xpath).text

        push_data = dict(product_name=product_text, product_image=product_img, product_price=product_price)

        data.append(push_data)

time.sleep(30)
driver.quit()

print(data)
#print(img_data)

