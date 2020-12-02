import unittest
from ..simplepuzzles import day_2


class Day2Test(unittest.TestCase):

    def test_process(self):
        input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        num_1, num_2 = day_2.process(input)
        self.assertEqual(num_1, 2)
        self.assertEqual(num_2, 1)


if __name__ == '__main__':
    unittest.main()
