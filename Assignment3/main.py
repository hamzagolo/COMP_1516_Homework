# Author: Marvin Neoh
from data import countries_and_capitals
from country import Country
import random


def main():
    """
    This function will try to create a list of Country objects using the countries_and_capitals tuple
    :return:
    """
    all_countries = []

    try:
        for country_and_capital in countries_and_capitals:
            country_object = Country(
                country_and_capital[0],
                country_and_capital[1],
                random.randint(1000000, 1000000000)
            )
            all_countries.append(country_object)

    except ValueError as value_error_message:
        print(f"oops {value_error_message}")

    for country in all_countries:
        country.print_details()

    for country in all_countries:
        country.birth()
        country.print_details()

    for country in all_countries:
        country.death()
        country.print_details()

    for country in all_countries:
        country.disaster()
        country.print_details()


if __name__ == "__main__":
    main()
