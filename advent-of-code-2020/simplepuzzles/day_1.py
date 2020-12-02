import os


def part_1():
    """ Find in a range of numbers two numbers which if added result in 2020.
    Then the result of multipling the two will be printed to the command line.
    """
    print("Solving day 1 part 1")
    # Call the function
    numbers = find_two_number_that_add_up_to(get_input(), 2020)
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
    numbers = find_three_number_that_add_up_to(get_input(), 2020)
    # Check, if two numbers have been found
    if (numbers == None):
        print("There are no numbers found that fullfill the condition.")
    else:
        (num_1, num_2, num_3) = numbers
        solution = num_1 * num_2 * num_3
        print("Solution: {} * {} * {} = {}".format(num_1, num_2, num_3, solution))


def get_input():
    # Absolute dir the script is in
    script_dir = os.path.dirname(__file__)
    # Join the relative path to the input file
    resource_path = os.path.join(script_dir, '../resources/Day1Input.txt')
    # Open the file
    with open(resource_path) as f:
        # Read all lines from the file. Per default we have now strings
        lines_as_string = [line.rstrip() for line in f]
        # As we expect numbers here and need them in order to do calculations lets map to int
        lines_as_int = list(map(int, lines_as_string))
        return lines_as_int


def find_two_number_that_add_up_to(numbers, target):
    for number in numbers:
        compatible_number = target - number
        if (compatible_number in numbers):
            return (compatible_number, number)


def find_three_number_that_add_up_to(numbers, target):
    for number in numbers:
        if (False):
            return (6, 4, 3)
