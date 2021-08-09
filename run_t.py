from commen import method
from data import data_t
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(2)
url=data_t.data.get("url")
username=data_t.data['username']
password=data_t.data["password"]
key=data_t.data.get("key")
result=method.seach(driver,key,url,username,password)
if key in result:
    print("搜索正确")
else:
    print("搜索错误")