# Author: Marvin Neoh
import re


def is_valid_license_plate(input_string):
    """
    This function checks if the input string is a valid license plate. The conditions are Six characters total:
    three letters then three digits, or three digits then three letters, or two letters, digit, space or hyphen,
     two digits, letter
    :return: True if the parameter matches the license plate pattern, false if it doesn't, boolean
    """

    # check the length of the input string

    if (re.match(r"^[A-Z]{3}[0-9]{3}$", input_string) or
            re.match(r"^[0-9]{3}[A-Z]{3}$", input_string) or
            re.match(r"^[A-Z]{2}[0-9] [0-9]{2}[A-Z]$", input_string) or
            re.match(r"^[A-Z]{2}[0-9]-[0-9]{2}[A-Z]$", input_string)):
        return True

    else:
        return False


def is_valid_python_variable_name(input_string):
    """
    This function checks if the input string is a valid python variable name. It should have between one and 32
     characters total: all characters must be lowercase letters or underscores, but no multiple underscore in a row
    :return: True if the parameter matches the criteria, false if it doesn't, boolean
    """
    if re.match(r"^[a-z](?!.*_{2,})(?:[a-z_]){0,31}$", input_string):
        return True
    else:
        return False


def is_valid_email_address(input_string):
    """
    This function checks if the input string is a valid email address. The username should have letters and underscores,
    and have between 1 and 256 characters. The domain name should have 1 to 32 characters, while the top domain should
    have 2 to 5 characters.
    :return: True if the parameter matches the criteria, false if it doesn't, boolean
    """
    email_data = re.split('@', input_string)
    username = email_data[0]
    domain_data = re.split('[.]', email_data[1])
    domain_name, top_level_domain = domain_data[0], domain_data[1]

    if (
            re.match(r"^(?!_)(?!.*_$)[a-zA-Z_]{1,256}$", username) and
            re.match(r"^[a-zA-Z]{0,31}$", domain_name) and
            re.match(r"^[a-zA-Z]{1,5}$", top_level_domain)
    ):
        return True

    else:
        return False


def is_valid_human_height(input_string):
    """
    This function checks if the input string is a valid human height. It should be between 2 to 8 feet and 0 to 11
    inches. The word "in" is an acceptable alternative to double quotation marks for inches.
    :return:
    """
    print(input_string)
    if re.match(r"^(?:[2-8]'(?:1[0-1]|[2-9]|0?[1-9])(\"|in))$", input_string):
        return True
    else:
        return False


def main():
    """
    This should not be called
    """
    pass


if __name__ == "__main__":
    main()
