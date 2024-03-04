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
    special_character_check = re.search("[^a-zA-Z0-9.]", filename)

    # checks if the filename has a length of 1 to 8, +4 to both numbers tom compensate for the length of the ".txt"
    # extension
    length_check = re.match("^.{5,12}$", filename)

    # checks if the file has a ".txt" extension
    file_extension_check = re.search(r".txt$", filename)

    if special_character_check or not length_check or not file_extension_check:
        while special_character_check or not length_check or not file_extension_check:
            filename = input("Please enter a valid filename: ")
            special_character_check = re.search("[^a-zA-Z0-9.]", filename)
            length_check = re.match("^.{5,12}$", filename)
            file_extension_check = re.search(r".txt$", filename)

    with open(filename, "w") as file:
        for country, capital in countries_capitals_dictionary.items():
            file.write(f"The capital of {country} is {capital}.\n")


def save_capitals():
    """
    This function creates multiple files and writes data into them that is based on certain patterns.
    """
    pass



def main():
    """
    This function does nothing, do not call this function
    """
    pass


if __name__ == "__main__":
    main()
