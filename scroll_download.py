from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select ,WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time , random ,requests

links_list = []
driver = webdriver.Chrome(service=Service('../chromedriver.exe')) # add your driver path
driver.get('https://www.digikala.com/')
driver.maximize_window()
wait = WebDriverWait(driver, 20)
action = ActionChains(driver)

search_box = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="base_layout_desktop_fixed_header"]/header/div[2]/div/div/div[1]/div/div/div[1]/div'))).click()
search_box_1 = wait.until(ec.element_to_be_clickable((By.XPATH, '//input[@name="search-input"]')))
search_box_1.send_keys('xiaomi mi a3'+Keys.ENTER)

while True:
    source = driver.page_source
    time.sleep(2)
    wait.until(ec.presence_of_element_located((By.TAG_NAME, 'html'))).send_keys(Keys.PAGE_DOWN)
    if source == driver.page_source:
        break

raw_links = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'section img')))
for row_link in raw_links:
    links_list.append(row_link.get_attribute('src'))

for link in links_list:
    print(link)
    with requests.get(link , stream=True) as r:
        with open(f'{str(random.randint(1,1000))}.jpg','wb') as p:
            for data in r.iter_content(1024):
                p.write(data)
