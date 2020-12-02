import timeit
from ..loadingdata import loading_text_files

def sled_rental_rule(password, letter, lower_bound, upper_bound):
    letter_count = password.count(letter)
    if lower_bound <= letter_count <= upper_bound:
        return True
    return False


def official_toboggan_rule(password, char, pos1, pos2):
    pos1_letter = password[pos1 - 1]
    pos2_letter = password[pos2 - 1]
    is_pos1_letter_correct = (pos1_letter == char)
    is_pos2_letter_correct = (pos2_letter == char)
    if is_pos1_letter_correct != is_pos2_letter_correct:
        return True
    return False


def process(string):
    sled_rental_valid_passwords = 0
    official_toboggan_valid_passwords = 0
    for line in string:
        rule, raw_char, password = line.split()
        char = raw_char[0]
        no1, no2 = rule.split('-')
        no1 = int(no1)
        no2 = int(no2)
        if sled_rental_rule(password, char, lower_bound=no1, upper_bound=no2):
            sled_rental_valid_passwords += 1
        if official_toboggan_rule(password, char, pos1=no1, pos2=no2):
            official_toboggan_valid_passwords += 1
    return sled_rental_valid_passwords, official_toboggan_valid_passwords


def day2():
    string = loading_text_files.read_lines("Day2Input.txt")
    sled_rental_valid_passwords, official_toboggan_valid_passwords = process(string)
    print(f'Number of sled rental passwords: {sled_rental_valid_passwords}')
    print(f'Number of official toboggan passwords: {official_toboggan_valid_passwords}')


if __name__ == '__main__':
   print(timeit.timeit(day2, number=1), 'seconds')