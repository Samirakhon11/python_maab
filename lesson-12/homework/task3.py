import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.demoblaze.com")
time.sleep(2)

laptop_button = driver.find_element(By.XPATH, "//a[@id='itemc' and text()='Laptops']")
laptop_button.click()
time.sleep(3)

laptop_data = []

while True:
    time.sleep(3)

    laptops = driver.find_element(By.CLASS_NAME, 'card-block')

    for laptop in laptops:
        try:
            name = laptop.find_element(By.TAG_NAME, "h4").text
            price = laptop.find_element(By.TAG_NAME, "h5").text
            description = laptop.find_element(By.CLASS_NAME, "card-text").text

            laptop_data.append({
                "name": name,
                "price": price,
                "description": description
            })
        except Exception as e:
            print("Skipping item due to error: ", e)

    try:
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()
        time.sleep(3)
    except:
        print("No more pages. Exiting...")
        break

with open("laptops.json", 'w', encoding="utf-8") as file:
    json.dump(laptop_data, file, indent=4, ensure_ascii=False)

print("Data scraped successfully and saved to laptops.json")

driver.quit() 