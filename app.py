from selenium import webdriver
import time

browser = webdriver.Chrome()
print("正在打开网页...")

time.sleep(2)
browser.get("http://www.baidu.com")

element = browser.find_element_by_id('kw')
element.send_keys('php')
element.send_keys(webdriver.common.keys.Keys.RETURN)

time.sleep(5)
# browser.close()




