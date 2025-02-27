import time
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar"
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

csv_file = open("amazon_products.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Product Name", "Price", "Rating", "Seller Name"])

while True:
    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    
    for product in products:
        try:
            product_name = product.find_element(By.XPATH, ".//h2[@aria-label]").get_attribute("aria-label")
        except:
            product_name = "N/A"
        
        try:
            price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        except:
            price = "N/A"
        
        try:
            rating = product.find_element(By.XPATH, ".//div[@class='a-row a-size-small']").text
        except:
            rating = "N/A"
        
        try:
            seller_name = product.find_element(By.XPATH, ".//span[@class='a-size-base-plus a-color-secondary']").text
        except:
            seller_name = "N/A"

        out_of_stock = product.find_elements(By.XPATH, ".//span[contains(text(),'out of stock')]")
        if out_of_stock:
            continue

        csv_writer.writerow([product_name, price, rating, seller_name])

    time.sleep(random.uniform(2, 5))

    try:
        next_button = driver.find_element(By.XPATH, "//li[@class='a-last']/a")
        next_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']")))
    except:
        break

csv_file.close()
driver.quit()

print("Scraping complete. Data saved to amazon_products.csv.")
