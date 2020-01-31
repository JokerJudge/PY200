import unittest
from py200_1_1 import Glass
# TODO - на typeError, на ValueError, на создание с большим occupied, чем capcity

class MyTestCase(unittest.TestCase):
    def test_init(self):
        self.assertRaises(TypeError, Glass, "str", 100) # передаем ссылку на объект Glass (как-будто функция)

if __name__ == '__main__':
    unittest.main()