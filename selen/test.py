from selenium import webdriver

driver = webdriver.Chrome("D:\Google\Chrome\Application\chromedriver.exe")
driver.get("http://www.baidu.com")

title = driver.title
a = "56432"
if a in title:
    print("dafzsdfaf")
else:
    print("165131231")
