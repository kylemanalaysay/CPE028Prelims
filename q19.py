import unittest

def name(x):
    x = 'PEDRO'
    return x

class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(name(),'KYLE')

if __name__ == "__main__":
    unittest.main()