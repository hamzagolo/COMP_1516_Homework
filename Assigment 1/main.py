# Author: Marvin Neoh
import project
import string


def main():
    """
    Calls print_json_countries_and_capitals(), get_list_of_countries_whose_nth_letter_is(),
    get_funny_case_capital_cities(), and get_doubled_letter_countries() functions.
    """

    project.print_json_countries_and_capitals()

    for number in range(1, 3):
        for letter in ['a', 'e', 'i', 'o', 'u']:
            print(project.get_list_of_countries_whose_nth_letter_is(number, letter))

    for letter in list(string.ascii_lowercase):
        print(project.get_funny_case_capital_cities(letter))

    print(project.get_doubled_letter_countries())


if __name__ == "__main__":
    main()
