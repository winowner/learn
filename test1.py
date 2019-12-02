"""
测试HTML5页面
"""
from time import sleep,ctime
from selenium import webdriver

from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)

# for i in range(100 ,500 , 100):
#     print(i)
#     try:
#         print("-----")
#         js = "window.scrollTo(0," + str(i) + ");"
#         print(js)
#
#     except:
#         pass
#     sleep(1)
# else:
#     print("time out")

dicA = {'a':'1','b':'2','c':'3'}
print('---'.join(dicA))
print('---'.join(dicA.values()))

a,b = 1,2
print(a,b)
