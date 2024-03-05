# Author: Marvin Neoh
from data import countries_and_capitals, countries, capitals, countries_capitals_dictionary
import assignment2 as a2
import re


def main():
    """
    This function calls the write_capitals_to_file() and save_capitals() function
    """
    a2.write_countries_capitals_to_file("123456.txt")

    a2.save_capitals()


if __name__ == "__main__":
    main()
