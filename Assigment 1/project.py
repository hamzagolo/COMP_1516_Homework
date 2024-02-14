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
        if country[n-1] == letter.lower() or country[n-1] == letter.upper():    # checks for both lower and upper case
            output.append(country)

    return output


def get_funny_case_capital_cities(letter):
    """
    This function creates and returns a list of capital cities that adhere to the funny case rule. A letter that
    immediately before and after the input letter is uppercased.
    :param letter: A character, str
    :return: List of capital cities in funny case, list
    """

    letter = letter.lower()     # ensures the function work even with an uppercase input

    output = []

    for capital in capitals:

        capital = capital.lower()

        if letter in capital:

            capital_list = list(capital)
            index = 0
            capital_list_length = len(capital_list)

            while index < capital_list_length:

                if capital_list[index] == letter:

                    capital_list[index] = capital_list[index].lower()

                    # ensures the letter immediately after the letter in within index
                    if index+1 < capital_list_length and capital_list[index+1] != letter:
                        capital_list[index+1] = capital_list[index+1].upper()

                    # ensures the letter immediately before the letter in within index
                    if index-1 >= 0 and capital_list[index-1] != letter:
                        capital_list[index-1] = capital_list[index-1].upper()

                index += 1

            output.append("".join(capital_list))

    return output


def get_doubled_letter_countries():
    """
    This function creates and returns a tuple of all the countries that have consecutive repeated letters in
    alphabetical order by the double letters
    :return: A tuple of countries, tuple
    """

    temp = []
    output = []

    for country in countries:
        index = 0
        while index < len(country)-1:
            if country[index] == country[index+1]:
                temp.append([country[index], country])
            index += 1

    temp.sort()

    for element in temp:
        output.append(element[1])

    return tuple(output)


if __name__ == "__main__":
    main()
