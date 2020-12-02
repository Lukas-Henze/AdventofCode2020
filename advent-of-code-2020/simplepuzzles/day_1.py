import os
from ..loadingdata import loading_text_files


def part_1():
    """ Find in a range of numbers two numbers which if added result in 2020.
    Then the result of multipling the two will be printed to the command line.
    """
    print("Solving day 1 part 1")
    # Call the function
    input = loading_text_files.read_line_as_numbers("Day1Input.txt")
    numbers = find_two_number_that_add_up_to(input, 2020)
    # Check, if two numbers have been found
    if (numbers == None):
        print("There are no numbers found that fullfill the condition.")
    else:
        (num_1, num_2) = numbers
        solution = num_1 * num_2
        print("Solution: {} * {} = {}".format(num_1, num_2, solution))


def part_2():
    print("Solving day 1 part 2")
    # Call the function
    input = loading_text_files.read_line_as_numbers("Day1Input.txt")
    numbers = find_three_number_that_add_up_to(input, 2020)
    # Check, if two numbers have been found
    if (numbers == None):
        print("There are no numbers found that fullfill the condition.")
    else:
        (num_1, num_2, num_3) = numbers
        solution = num_1 * num_2 * num_3
        print("Solution: {} * {} * {} = {}".format(num_1, num_2, num_3, solution))


def find_two_number_that_add_up_to(numbers, target):
    for number in numbers:
        compatible_number = target - number
        if (compatible_number in numbers):
            return (compatible_number, number)


def find_three_number_that_add_up_to(numbers, target):
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if(x+y+z == 2020):
                    return(x, y, z)
