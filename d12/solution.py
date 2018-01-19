"""
Solution to d12 - January 18 2018
"""
import sys
import unittest


#for testing
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(iterative2(4), 5)
    def test2(self):
        self.assertEqual(iterative3(4), 7)

#if take 1 or 2 steps
def iterative2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b
 
#if allowed to take 3 steps
def iterative3(n):
    a, b, c = 0, 0, 1
    for _ in range(n):
        a, b, c = b, c, a+b+c
    return c
 
#Main driver
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        print(iterative2(4))
        print(iterative3(5))
