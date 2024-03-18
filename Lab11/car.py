# Author: Marvin Neoh


class Car:
    """
    Represents a car in a car lot
    """

    def __init__(self, make, model, year, cost, price_usd):
        """
        initializes the car details
        :param make: Make of the car, str
        :param model: Model of the car, str
        :param year: Year the car was manufactured, int
        :param cost: Cost of the car, int
        :param price_usd: Price of the car, int
        """
        self._make = make
        self._model = model
        self._year = year
        self._cost = cost
        self._price_usd = price_usd

    def calc_profit(self):
        """
        Returns the projected profit in USD.
        """
        profit = self._price_usd - self._cost

        return profit

    def get_details(self):
        """
        This function returns a string with the details of the car
        :return: details of the car, str
        """
        car_details = f"{self._year} {self._make} {self._model} for sale for ${self._price_usd} USD"

        return car_details

    def reduce_price(self, reduction):
        """
        This functions reduces the price of a vehicle by the input amount
        """

        self._price_usd = self._price_usd - reduction


def main():
    pass


if __name__ == "__main__":
    main()
