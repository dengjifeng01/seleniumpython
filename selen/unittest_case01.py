#coding=utf-8

import unittest

class Test(unittest.TestCase):
    def test001(self):
        a = 1+2
        if a == 3:
            return True
        else:
            return False

    def test002(self):
        self.assertFalse(self.test001(),"error!!!")

    def tearDown(self):
        for aaa,bbb in self._outcome.errors:
            if bbb != None:
                print(bbb)
        name = self._testMethodName
if __name__ == "__main__":
    unittest.main()