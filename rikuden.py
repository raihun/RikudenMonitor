# -*- coding: utf-8 -*-
import time
from re import findall
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Setting
userid = 'ID'
userpw = 'PASSWORD'

options = Options()
options.add_argument('--headless')  # Chrome画面を表示/非表示
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://mieruka.rikuden.co.jp/OI008_DOC/contents/login/')

# ログイン処理
driver.implicitly_wait(5)
element = driver.find_element_by_name('riyoshaid')
element.send_keys(userid)
element = driver.find_element_by_name('passwd')
element.send_keys(userpw)
element.send_keys(Keys.RETURN)

# ページ遷移
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.invisibility_of_element_located((By.ID, "load--dialog")))
driver.find_element_by_id('oi008_ba002_scr001-siyoryohikakubutton').click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.invisibility_of_element_located((By.ID, "load--dialog")))
driver.find_element_by_id('oi008_ka006_scr001-jibun_hikuraberubutton').click()

# 使用量 抽出
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.invisibility_of_element_located((By.ID, "load--dialog")))
driver.execute_script("Array.prototype.forEach.call(document.getElementsByClassName('jqplot-point-label'),function(e){e.style.display='block'})")
elements = driver.find_elements_by_xpath('//div[@class="oi8-graph-balloon"]/table/tbody/tr[2]/td')[::2]
for e in elements:
    kWh = findall(r'(.*)kWh', e.text)[0]
    print(kWh)

# ログアウト処理
driver.find_element_by_id('btn-logout').click()

# 終了処理
time.sleep(5)
driver.quit()
