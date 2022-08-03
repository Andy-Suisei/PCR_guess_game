import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

chrome_options = Options()
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)


driver.get('https://pcredivewiki.tw/Character')
time.sleep(3)
for _ in range(23):
    driver.execute_script('window.scrollBy(0, 200);')
    time.sleep(0.5)
img = driver.find_elements(By.CLASS_NAME, 'img-fluid')
name = driver.find_elements(By.CLASS_NAME, 'text-muted')
img_list = []
name_list = []
for i in img:
    img_list.append(i.get_attribute('src'))
for i in name:
    name_list.append(i.text)
name_list = name_list[:-2]
img_list = img_list[1:]

for i in range(len(img_list)):
    with open(f'princess_img/{name_list[i]}.png', 'wb') as f:
        f.write(requests.get(img_list[i]).content)

driver.close()
