from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get('https://www.daraz.com.bd/products/new-stylish-eyewear-frames-for-men-and-women-trendy-durable-and-comfortable-i490604933-s2373248417.html')

#to avoid caching issue
driver.refresh()

driver.maximize_window()
get_window_height = driver.execute_script('return document.body.scrollHeight')
print(get_window_height)

for i in range(get_window_height):
    driver.execute_script(f'window.scrollTo(0,{i})')
    time.sleep(1)

comment = driver.find_elements(By.CLASS_NAME,'content')

for j in comment:
    print(j.text)
time.sleep(30)
driver.quit()