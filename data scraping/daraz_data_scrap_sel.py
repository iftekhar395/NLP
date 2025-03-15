from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

#time.sleep(300)

for x in range(1,40):
    castX = str(x)
    image_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+castX+']/div/div/div[1]/div/a/div/img'
    name_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+castX+']/div/div/div[2]/div[2]/a'
    price_xpath = '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+castX+']/div/div/div[2]/div[3]/span'
    
    #driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, price_xpath)))
    #time.sleep(20)
    product_img = driver.find_element(By.XPATH,image_xpath).get_attribute('src')
    
    product_text = driver.find_element(By.XPATH,name_xpath).text
    product_price = driver.find_element(By.XPATH,price_xpath).text

    push_data = dict(product_name=product_text, product_image=product_img, product_price=product_price)

    data.append(push_data)

time.sleep(300)
driver.quit()

print(data)






































