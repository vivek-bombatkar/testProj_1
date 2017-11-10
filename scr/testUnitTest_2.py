import unittest

def strComp(s1,s2):
    return (s1==s2)

class ut(unittest.TestCase):
    def testStrComp(self):
        self.failUnless(strComp("A","A"))

def main():
    unittest.main()

if __name__=='__main__':
    main()

