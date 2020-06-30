import unittest
import calculation


class MyTestCase(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = calculation.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 4)

    def test_add_num_double_raise(self):
        cal = calculation.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()
