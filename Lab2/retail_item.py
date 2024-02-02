
def main():

    item_description = get_retail_item_description()
    quantity_sold = get_number_of_purchased_items()
    price_per_unit_usd = get_price_usd_per_unit()
    tax_rate = get_tax_rate()

    subtotal_usd = calculate_subtotal_usd(price_per_unit_usd, quantity_sold)
    tax_amount_usd = calculate_tax_usd(subtotal_usd, tax_rate)
    total_price_usd = calculate_total_usd(subtotal_usd, tax_amount_usd)

    # Sales receipt portion of code, \n new line used for output clarity on the console
    print("\nSales Receipt:")
    print("Item Description:", item_description)
    print("Number of Purchased items:", quantity_sold)
    print("Unit Price(usd):", price_per_unit_usd)
    print("Tax Rate:", tax_rate)
    print("Subtotal:", subtotal_usd, "(usd)")
    print("Tax:", tax_amount_usd, "(usd)")
    print("Total:", total_price_usd, "(usd)")


def get_retail_item_description():
    """
    prompts user to enter retail item description and returns it
    :return: retail item description, string
    """
    item_description = input("Enter retail item description: ")

    return item_description


def get_number_of_purchased_items():
    """
    prompts user to enter the quantity sold and returns it
    :return: number of items purchased, int
    """
    number_of_purchased_items = input("Enter quantity purchased: ")

    return number_of_purchased_items


def get_price_usd_per_unit():
    """
    prompts the user to enter the price in American dollars and returns it
    :return: price in American dollars, float
    """
    price_per_unit_usd = input("Enter price per unit(usd): ")

    return price_per_unit_usd


def get_tax_rate():
    """
    Prompts the user to enter the tax rate as a float and returns it
    :return: tax rate, float
    """
    tax_rate = input("Enter tax: ")

    return tax_rate


def calculate_subtotal_usd(price_usd, quantity_sold):
    """
    calculates and returns the subtotal amount in American dollars
    :param price_usd: the price of a product in usd, float
    :param quantity_sold: the quantity of products sold, int
    :return: subtotal amount in usd, which is the price multiplied by quantity sold, float
    """
    subtotal_usd = float(price_usd)*float(quantity_sold)
    # float() used to make sure the var type is good to be mathed on

    return subtotal_usd


def calculate_tax_usd(subtotal_usd, tax_rate):
    """
    calculates and returns the tax amount in American dollars
    :param subtotal_usd: the subtotal of the order in usd, float
    :param tax_rate: tax rate, float
    :return: tax_amount in usd, calculated by multiplying the subtotal amount by the tax rate, float
    """
    tax_amount = float(subtotal_usd)*float(tax_rate)
    # float() used to make sure the var type is good to be mathed on

    return tax_amount


def calculate_total_usd(subtotal_usd, tax_amount):
    """
    calculates the total amount given a subtotal and tax amount
    :param subtotal_usd: subtotal amount in usd, float
    :param tax_amount: tax amount in usd, float
    :return: total price, float
    """
    total_usd = subtotal_usd+tax_amount

    return total_usd


if __name__ == "__main__":
    main()