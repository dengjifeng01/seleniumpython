# coding=utf-8

from selenium import webdriver
from time import sleep
import configparser
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome("D:\Google\Chrome\Application\chromedriver.exe")

#初始化浏览器，输入url
def open_url():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()

#定位用户信息，获取element
def read_ini(ff):
    cf = configparser.ConfigParser()
    cf.read("us.ini")
    data = cf.get("username",ff)
    by = data.split(">")[0]
    value = data.split(">")[1]
    try:
        if by == "id":
            dddd = driver.find_element_by_id(value)
        elif by == "xpath":
            dddd = driver.find_element_by_xpath(value)
    except:
        print("没有找到对应元素")
        return None
    return dddd

#打开保存测试用户的文件
def open_file():
    f = open("123.txt","r")
    a = f.readlines()
    return a

#截取验证码
def code():
    driver.save_screenshot('E:/123.png')
    code_element = read_ini("yzm")
    left = code_element.location["x"]
    top = code_element.location["y"]
    width = code_element.size["width"] + left
    height = code_element.size["height"] + top

    im = Image.open("E:/123.png")
    img = im.crop((left,top,width,height))
    img.save("E:/1234.png")

#识别验证码
def sb():
    r = ShowapiRequest("http://route.showapi.com/184-1", "62626", "d61950be50dc4dbd9969f741b8e730f5")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    r.addFilePara("image", "E:/1234.png") #文件上传时设置
    res = r.post()
    text = res.json()["showapi_res_body"]["Result"]
    return text


def main():
    a = open_file()
    for each in a:
        e = each.split(",")[0]
        u = each.split(",")[1]
        p = each.split(",")[2]
        open_url()
        sleep(2)
        code()
        read_ini("user_email").send_keys(e)
        read_ini("user_name").send_keys(u)
        read_ini("password").send_keys(p)
        read_ini("code_input").send_keys(1111)
        if read_ini("code_error") != None:
            driver.save_screenshot("E:/codeerror.png")
        sleep(2)

if __name__ == "__main__":
    main()