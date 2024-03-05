# Author: Marvin Neoh
from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import re


def write_countries_capitals_to_file(filename):
    """
    This function takes a valid filename, creates the file, and writes the data from countries_capitals_dictionary into
    the file.
    :param filename: Name of the file to be created, str
    """
    # checking if filename contains only letters or digits
    special_character_check = check_characters(filename)

    # checks if the filename has a length of 1 to 8, +4 to both numbers tom compensate for the length of the ".txt"
    # extension
    length_check = check_length(filename)

    # checks if the file has a ".txt" extension
    file_extension_check = check_file_extension(filename)

    # checks if any error is raised and reloops if there are any unsatisfied conditions
    while special_character_check or not length_check or not file_extension_check:
        filename = input("Please enter a valid filename: ")
        special_character_check = check_characters(filename)
        length_check = check_length(filename)
        file_extension_check = check_file_extension(filename)

    with open(filename, "w") as file:
        for country, capital in countries_capitals_dictionary.items():
            file.write(f"The capital of {country} is {capital}.\n")


def check_characters(string):
    """
    This function checks if the filename contains any special characters
    :param string: String to be checked, str
    :return: Returns a Match object if there are any special characters, returns None otherwise
    """
    output = re.search("[^a-zA-Z0-9.]", string)

    return output


def check_length(string):
    """
    This function checks if the string has total length of 5 to 12 characters, taking into account the .txt exension
    :param string: String to be checked, str
    :return: Returns a Match object if the string is between 5 and 12 characters, returns None otherwise
    """
    output = re.match("^.{5,12}$", string)

    return output


def check_file_extension(string):
    """
    Checks if the string given ends with ".txt"
    :param string: String to be checked, str
    :returns: Returns a Match object if there is .txt extension, returns None otherwise
    """
    output = re.search(r".txt$", string)

    return output


def save_capitals():
    """
    This function creates multiple files and writes data into them that is based on certain patterns.
    """

    # this segment of code will create the file that contains capitals with three consecutive vowels
    with open("vowel_vowel_vowel.txt", "w") as file:
        for capital in capitals:
            if re.search("[aeiouAEIOU]{3,}", capital):
                file.write(f"{capital}\n")

    # this segment of code will create the file that contains capitals with three consecutive consonants
    with open("cons_cons_cons.txt", "w") as file:
        for capital in capitals:
            if re.search("[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]{3,}", capital):
                file.write(f"{capital}\n")

    # this segment of code will create the file the contains capitals that have an i somewhere before e
    with open("i_before_e.txt", "w") as file:
        for capital in capitals:
            if re.search("i.*e", capital):
                file.write(f"{capital}\n")

    # this segment of code will create the file the contains capitals that starts and ends with the letter a
    with open("a_a.txt", "w") as file:
        for capital in capitals:
            if re.search("^A", capital) and re.search("a$", capital):
                file.write(f"{capital}\n")

    # this segment of code will create the file that contains capitals that ends with a vowel
    with open("end_with_vowel.txt", "w") as file:
        for capital in capitals:
            if re.search("[aeiouAEIOU]$", capital):
                file.write(f"{capital}\n")

    # this segment of code will create the file that contains capitals that has an apostrophe, a space, or x
    with open("weird.txt", "w") as file:
        for capital in capitals:
            if re.search("[' x]", capital):
                file.write(f"{capital}\n")

    # this segment of code will create the file that contains capitals taht does not start with a-e, l-p, or s
    with open("not_start.txt", "w") as file:
        for capital in capitals:
            if re.search("^[^a-el-psA-EL-PS]", capital):
                file.write(f"{capital}\n")


def main():
    """
    This function does nothing, do not call this function
    """
    print("This function does nothing, do not call this function")


if __name__ == "__main__":
    main()
