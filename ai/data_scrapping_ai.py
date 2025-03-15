from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Image source taking time to load
driver = webdriver.Firefox()
driver.get('https://www.daraz.com.bd/mens-eyeglasses/')

# Scroll to ensure images are loaded
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)  # Give time for images to load

data = []

for x in range(1, 41):
    castX = str(x)
    image_xpath = f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{castX}]/div/div/div[1]/div/a/div/img'
    name_xpath = f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{castX}]/div/div/div[2]/div[2]/a'
    price_xpath = f'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[{castX}]/div/div/div[2]/div[3]/span'

    try:
        # Wait until the elements are visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, image_xpath)))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name_xpath)))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, price_xpath)))

        product_img_element = driver.find_element(By.XPATH, image_xpath)

        # Scroll to element to force image load
        driver.execute_script("arguments[0].scrollIntoView();", product_img_element)
        time.sleep(1)  # Small delay to ensure it loads

        product_img = product_img_element.get_attribute('src')
        product_text = driver.find_element(By.XPATH, name_xpath).text
        product_price = driver.find_element(By.XPATH, price_xpath).text

        push_data = dict(product_name=product_text, product_image=product_img, product_price=product_price)
        data.append(push_data)

    except Exception as e:
        print(f"Error fetching data for item {x}: {e}")

time.sleep(3)
driver.quit()

print(data)