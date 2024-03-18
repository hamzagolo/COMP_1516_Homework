# Author: Marvin Neoh
from car import Car


def main():
    """

    """
    car1 = Car("Honda", "Civic", 2020, 15000.0, 20000.0)
    print(car1.get_details())
    print("First Car's Initial Profit is $%.2f USD" % car1.calc_profit())
    car1.reduce_price(1000.0)
    print("First Car's New Profit is $%.2f USD\n" % car1.calc_profit())

    car1 = Car("BMW", "M3", 2019, 30000.0, 50000.0)
    print(car1.get_details())
    print("Second Car's Initial Profit is $%.2f USD" % car1.calc_profit())
    car1.reduce_price(5000.50)
    print("Second Car's New Profit is $%.2f USD" % car1.calc_profit())


if __name__ == "__main__":
    main()
