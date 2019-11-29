from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()

browser.implicitly_wait(10)
browser.get('http://192.168.80.208:8080/FOV-MA/login')
# assert '百度' in browser.title

username = browser.find_element_by_id('userName')  # Find the search box
username.send_keys('admin')
password = browser.find_element_by_id('password')
password.send_keys('admin' + Keys.ENTER)

eventList = browser.find_element_by_name('warningEventList')
eventList.click()

highQuery = browser.find_element_by_id('simpleQuery')
highQuery.click()

alarmType = browser.find_element_by_id('alarmType')
alarmType
# attribute = browser.find_element_by_id("kw").get_attribute('type')
# print(attribute)


# above = browser.find_element(By.PARTIAL_LINK_TEXT, '设置')
# ActionChains(browser).move_to_element(above).perform()

# browser.quit()