#coding=utf-8
import unittest
from selenium import webdriver
import HTMLTestRunner
import os
from time import sleep
class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("D:\Google\Chrome\Application\chromedriver.exe")
        self.driver.maximize_window()
        url = "http://www.baidu.com"
        self.driver.get(url)
        print("前置")

    def test00(self):
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("123")
        driver.find_element_by_id("su").click()


    def test01(self):
        driver = self.driver
        try:
            d = driver.find_element_by_id("dsfsfd").click()
        except:
            return False
        sleep(3)

    def test02(self):
        test01 = self.test01()
        self.assertTrue(test01,"error!!!")

    def tearDown(self):
        sleep(2)
        for method_name,error in self._outcome.errors:
            print(method_name,error)
        print("后置")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test("test00"))
    suite.addTest(Test("test01"))
    suite.addTest(Test("test02"))
    fp = open("./ress.html","wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="这是第一份测试报告",
                                           description="用例执行情况：")
    runner.run(suite)
    fp.close()