# Author: Marvin Neoh
from data import countries_and_capitals, countries, capitals


def main():
    """
    does nothing
    :return:
    """
    print("I should not be called")


def print_json_countries_and_capitals():
    """
    This function prints each country and its capital in JSON format
    :return: A list of countries and capitals, list
    """
    count = 0
    output = []

    while count < len(countries_and_capitals):
        output.append({
            "country_name": countries_and_capitals[count][0],
            "capital_city": countries_and_capitals[count][1]
        })
        count += 1

    # concern 1: quotation marks is single instead of doule
    # concern 2: output in console does not have the proper spacing
    print(output)


def get_list_of_countries_whose_nth_letter_is(n, letter):
    """
    This function creates and returns a list of all countries whose nth letter matches the letter in the parameter.
    :param n: The nth letter, int
    :param letter: Character, str
    :return: List of all countries, list
    """

    output = []

    for country in countries:
        if country[n-1] == letter.lower() or country[n-1] == letter.upper():
            output.append(country)

    return output

def get_funny_case_capital_cities(letter):
    """
    This function creates and returns a list of capital cities that
    :param letter:
    :return:
    """
    pass


def get_doubled_letter_countries():
    """
    This function creates and retuns a tuple of all the countries that have consecutive repeated letters in alphabetical
    order by the doule letters
    :return:
    """
    pass


if __name__ == "__main__":
    main()
