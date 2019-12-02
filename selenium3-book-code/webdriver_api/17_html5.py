"""
测试HTML5页面
"""
from time import sleep,ctime
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://videojs.com/")

# for i in range(100 ,4000 ,100):
#     try:
#         js = "window.scrollTo(0," + str(i) + ");"
#         print(js)
#         driver.execute_script(js)
#     except:
#         pass
#     sleep(1)
# else:
#     print("time out")

js = "window.scrollTo(0,3900);"
driver.execute_script(js)

video = driver.find_element_by_id("preview-player_html5_api")
# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

driver.find_element_by_id("preview-player").click()
# playBtn = driver.find_element_by_class_name("vjs-big-play-button")
# playBtn.click()
# 播放视频
print("load")
driver.execute_script("arguments[0].load()", video)

# 播放视频
print("start")
driver.execute_script("arguments[0].play()", video)

# 播放15秒钟
sleep(15)

# 暂停视频
print("stop")
driver.execute_script("arguments[0].pause()", video)

# driver.quit()