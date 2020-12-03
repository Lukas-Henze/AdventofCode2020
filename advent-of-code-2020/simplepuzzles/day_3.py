
from ..loadingdata import loading_text_files


def day_3(right, down):
    lines = loading_text_files.read_lines("Day3Input.txt")
    return get_tree_count(lines, right, down)

def get_tree_count(map, right, down):
    width = len(map[0])
    trees = 0
    for row in range (0, len(map), down):
        column = (right*row//down) % width
        if map[row][column] == "#":
            trees += 1
    return trees

def part_1():
    print(day_3(3,1))

def part_2():
    print(day_3(3,1)*day_3(1,1)*day_3(5,1)*day_3(7,1)*day_3(1,2))
