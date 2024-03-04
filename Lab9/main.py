# Author: Marvin Neoh
import re


def is_valid_license_plate(input_string):
    """
    This function checks if the input string is a valid license plate. The conditions are Six characters total:
    three letters then three digits, or three digits then three letters, or two letters, digit, space or hyphen,
     two digits, letter
    :return: True if the parameter matches the license plate pattern, false if it doesn't, boolean
    """

    # check the length after stripping space and hyphen, has to be equal to 6
    input_string = input_string.strip(" -")
    if len(input_string) != 6:
        return False

    # check if all letters are uppercased
    if not input_string == input_string.upper():
        return False


    # check if it follows the pattern of 3 letters and 3 digits, and the reverse
    # check if

    pass


def is_valid_pythong_variable_name(input_string):
    """
    This function checks if the input string is a valid python variable name. It should have between one and 32
     characters total: all characters must be lowercase letters or underscores, but no multiple underscore in a row
    :return: True if the parameter matches the criteria, false if it doesn't, boolean
    """
    pass


def is_valid_email_address(input_string):
    """
    This function checks if the input string is a valid email address. The username should have letters and underscores,
    and have between 1 and 256 characters. The domain name should have 1 to 32 characters, while the top domain should
    have 2 to 5 characters.
    :return: True if the parameter matches the criteria, false if it doesn't, boolean
    """

    pass


def is_valid_human_height(input_string):
    """
    This function checks if the input string is a valid human height. It should be between 2 to 8 feet and 0 to 11
    inches. The word "in" is an acceptable alternative to double quation marks for inches.
    :return:
    """



    pass


def main():
    pass


if __name__ == "__main__":
    main()
