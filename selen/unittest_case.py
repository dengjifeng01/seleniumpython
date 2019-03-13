#coding=utf-8
import unittest

class TTT(unittest.TestCase):
    #所有用例的前置条件，只执行一次。
    @classmethod
    def setUpClass(cls):
        print("所有case的前置条件")
    #所有用例的后置条件，只执行一次。
    @classmethod
    def tearDownClass(cls):
        print("所有case的后置条件")

    #前置条件，每一条用例执行之前都需要执行一次。
    def setUp(self):
        print("这是前置条件")
    #后置条件，每一条用例执行之前都需要执行一次。
    def tearDown(self):
        print("这是后置条件")

    #用例1
    def testcase01(self):
        print("这是1条case")
    #用例2
    def testcase02(self):
        print("这是2条case")

if __name__ == "__main__":
    #执行所有用例
    suite = unittest.TestLoader().loadTestsFromTestCase(TTT)
    unittest.TestRunner().run(suite)