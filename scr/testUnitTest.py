import unittest
# DID NOT WORKED
class testCls(unittest.TestCase):

    def fun1(self):
        self.assertEqual('vidhi'.upper(),'1VIDHI')

    def fun2(self):
        self.assertEqual("a","A")

def main():
    unittest.main()

if __name__ == '__main__':
    main()