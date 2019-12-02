"""
*  switch_to.frame()  进入表单
*  switch_to.default_content()  退出表单至根页面
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://www.126.com")
sleep(2)

frame1 = driver.find_element_by_xpath("//div[@class='login tab-1']/div[@class='new-loginFunc']/div[@id='lbNormal']")
frame1.click()

login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)

# emailName = driver.find_element_by_xpath("//form[@id='login-form']/div[@class='m-container']/div[@id='account-box']/div[@class='u-input box']/input[@name='email']")
emailName = driver.find_element_by_name("email")
# emailName = driver.find_element_by_class_name('j-inputtext dlemail j-nameforslide')
# emailName.click()
emailName.send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
# driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

# driver.quit()
