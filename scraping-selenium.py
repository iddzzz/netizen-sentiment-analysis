import pandas as pd
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# print("Enter the month in number (e.g. 01, 02, etc)!")
# bulan = input('= ')
bulan = '12'

options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\Saidzzz\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')
options.headless = True # To make browser disappear

s = Service(r"D:/physics/python/chromedriver.exe")

driver = webdriver.Chrome(service=s, options=options)
# driver.get(f"https://twitter.com/search?q=(ahmadiyah)%20until%3A2021-{int(bulan) + 1}-01%20since%3A2021-{bulan}-01&src=typed_query&f=live")
driver.get(f"https://twitter.com/search?q=(ahmadiyah)%20until%3A2022-01-01%20since%3A2021-{bulan}-01&src=typed_query&f=live")

wait = WebDriverWait(driver, 10)
time.sleep(5)

try:
    wait.until(ec.presence_of_element_located(
        (By.XPATH, '//div[@class="css-1dbjc4n r-j5o65s r-qklmqi r-1adg3ll r-1ny4l3l"]')))
except NoSuchElementException as why:
    print("No element ternyata")
    driver.close()

data = ['Test (delete this)']
i = 1

# To check if the tweet is the last one, the upper bound is 120
none_count = 0

while True:
    try:
        wait.until(
            ec.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]')),
            message="No element article"
        )
        time.sleep(1)
        tweets = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')

        for tweet in tweets:
            text = tweet.text
            if len(data) > 20:
                if text in data[-20:]:
                    none_count += 1
                else:
                    data.append(text)
                    print('-', text.split('\n')[0], '|', text.split('\n')[3])
                    none_count = 0
            else:
                if text in data:
                    none_count += 1
                else:
                    data.append(text)
                    print('-', text.split('\n')[0], '|', text.split('\n')[3])
                    none_count = 0

        if none_count >= 120:
            print("No data remaining. All data has been scraped")
            break

        ActionChains(driver).key_down(Keys.PAGE_DOWN).key_up(Keys.PAGE_DOWN).perform()
        print(f'Iteration: {i} | Data Count: {len(data)} | None Count: {none_count}')

        i += 1

        time.sleep(2)

    except Exception as wow:
        print("Something wrong")
        print(wow)
        break

time.sleep(5)

data.pop(0)
df = pd.DataFrame({'Tweet': data})
df.to_csv(f"{os.path.join(os.path.realpath(os.getcwd()), 'data', 'tweet')}{bulan}.csv")

driver.close()