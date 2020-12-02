import unittest
from ..simplepuzzles import day_1, day_2


class Day1Test(unittest.TestCase):

    def test_find_two_number_that_add_up_to(self):
        input = [1721, 979, 366, 299, 675, 1456]
        (num_1, num_2) = day_1.find_two_number_that_add_up_to(input, 2020)
        self.assertEqual(num_1 * num_2, 514579)

    def test_find_three_number_that_add_up_to(self):
        input = [1721, 979, 366, 299, 675, 1456]
        (num_1, num_2, num_3) = day_1.find_three_number_that_add_up_to(input, 2020)
        self.assertEqual(num_1 * num_2 * num_3, 241861950)


if __name__ == '__main__':
    unittest.main()
