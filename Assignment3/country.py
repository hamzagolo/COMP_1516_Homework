# Author: Marvin Neoh

class Country:

    def __init__(self, country_name, capital_name, population):
        """
        Initializes the country class
        :param country_name: Name of the country, str
        :param capital_name: Name of the country's capital, str
        :param population: NUmber of people in the country, int
        """
        self._country_name = country_name
        self._capital_name = capital_name

        if population >= 2000000:
            self._population = population
        else:
            raise ValueError(f"Population {population} is too low")

    def print_details(self):
        """
        Prints the details of the country
        """
        print(f"The capital of {self._country_name} (pop. {self._population}) is {self._capital_name.upper()}")

    def birth(self):
        """
        This function adds 1 to the country's population
        """
        self._population += 1

    def death(self):
        """
        This function subtracts 1 to the country's population
        """
        self._population -= 1

    def disaster(self):
        """
        This function subtracts 100 million people from the population
        """
        # using the max function so the country's population does not fall below 0
        self._population = max(self._population - 100000000, 0)


def main():
    """
    This function does nothing
    """
    print("This function does nothing, do not call this function")


if __name__ == "__main__":
    main()
