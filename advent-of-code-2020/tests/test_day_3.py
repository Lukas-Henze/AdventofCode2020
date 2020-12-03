import unittest
from ..simplepuzzles import day_3


class Day3Test(unittest.TestCase):

    def test_get_tree_count(self):
        input = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"
        ]
        self.assertEqual(day_3.get_tree_count(input,3,1), 7)
        self.assertEqual(day_3.get_tree_count(input,1,1), 2)
        self.assertEqual(day_3.get_tree_count(input,5,1), 3)
        self.assertEqual(day_3.get_tree_count(input,7,1), 4)
        self.assertEqual(day_3.get_tree_count(input,1,2), 2)


if __name__ == '__main__':
    unittest.main()
