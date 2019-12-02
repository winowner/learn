"""
* send_keys() 指定文件上传路径。
"""
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

file_path = os.path.abspath('./files/')
print(file_path)
driver = webdriver.Chrome()
driver.maximize_window()
# upload_page = 'file:///' + file_path + 'upfile.html'
# print(upload_page)
upload_page = 'http://192.168.80.208:8080/FOV-MA/index'
driver.get(upload_page)

username = driver.find_element_by_id('userName')  # Find the search box
username.send_keys('admin')
password = driver.find_element_by_id('password')
password.send_keys('admin' + Keys.ENTER)
sleep(3)
navigationMenu = driver.find_element_by_class_name('navigation-safety')
ac = ActionChains(driver)
ac.move_to_element(navigationMenu).perform()
sleep(1)
nationStandard = driver.find_element_by_name('nationStandardListPage')
nationStandard.click()
sleep(1)

ac.move_by_offset(-140, 0).perform()

driver.find_element_by_xpath('//button[@id="simpleSafetyAdd"]/span').click()
driver.find_element_by_id('name').send_keys('clcTest')
driver.find_element_by_id('docNum').send_keys('clc-1')
driver.find_element_by_id('releaseTime').send_keys('2019-10-29')

# 定位上传按钮，添加本地文件
driver.find_element_by_id("file").send_keys(file_path + '用户手册（GB8567——88）.doc')
# ……

sleep(1)
driver.find_element_by_id('operSafetyList').click()

sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[3]/div/table/tbody/tr[2]/td[8]/a[3]').click()

sleep(1)
# driver.find_element_by_xpath('//button[text()="确定"]').click()
driver.find_element_by_xpath("//button[contains(text(),'确定')]").click()