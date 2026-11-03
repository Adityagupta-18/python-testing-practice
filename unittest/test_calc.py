import unittest
from calc import add, sub, mul, div

class Testcalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(50,2),52)
        self.assertEqual(add(0,2),2)
        self.assertEqual(add(-3,28),25)

    def test_mul(self):
        self.assertEqual(mul(3,4),12)
        self.assertEqual(mul(7,-6),-42)

    def test_div(self):
        # self.assertRaises(ValueError, div,10,0)
        with self.assertRaises(ValueError):
            div(45,0)





if __name__=="__main__":
    unittest.main()