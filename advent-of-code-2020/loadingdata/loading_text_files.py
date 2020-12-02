import os


def read_lines(filename):
    """ Opens the file with the given name from the resource folder and retunrs all lines as a list of strings
    """
    # Absolute dir the script is in
    script_dir = os.path.dirname(__file__)
    # Join the relative path to the input file
    resource_path = os.path.join(script_dir, '../resources/' + filename)
    # Open the file
    with open(resource_path) as f:
        # Read all lines from the file. Per default we have now strings
        return [line.rstrip() for line in f]


def read_line_as_numbers(filename):
    """ Opens the file with the given name from the resource folder and retunrs all lines as a list of numbers
    """
    # As we expect numbers here and need them in order to do calculations lets map to int
    return list(map(int, read_lines(filename)))
