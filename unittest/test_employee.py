import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1=Employee('Aditya','Gupta',152010)

    def test_email(self):
        self.assertEqual(self.emp1.email(),'Aditya_Gupta@gmail.com')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname(),'Aditya Gupta')


if __name__=="__main__":
    unittest.main()