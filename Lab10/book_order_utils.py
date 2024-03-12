# Author: Marvin Neoh
import re
import os


def validate_book_order_details(order_num, title, author, isbn, year_pub, quantity, cost_cad):
    """
    This function validates each of the order details inputted
    :param order_num: Order number, str
    :param title: Title of book, str
    :param author: Author of book, str
    :param isbn: ISBN of book, str
    :param year_pub: The year the book was published, str
    :param quantity: Number of copies purchased, str
    :param cost_cad: Price of book, str
    """
    # Order Number: one or more integer values
    if re.search(r"[^0-9]+", order_num):
        raise ValueError("Order Number is invalid")

    # Title: One or more lower or uppercase letters
    if not re.search(r"^[A-Za-z ]+$", title):
        raise ValueError("Title is invalid")

    # Author: Zero or more lower or upper case letter with apostrophe
    if not re.search(r"^[A-Za-z\s' ]*$", author):
        raise ValueError("Author is invalid")

    # ISBN: Must be integer
    if not re.search(r"^\d+$", isbn):
        raise TypeError("ISBN must be an integer")

    # ISBN: Must be between 4 and 20 digits
    if not re.search(r"^\d{4,20}$", isbn):
        raise ValueError("ISBN is invalid")

    # Year Published: Must be integers
    if not re.search(r"^\d+$", year_pub):
        raise TypeError("Year must be an integer")

    # Year Published: Must be 4 digits exactly
    if not re.search(r"^\d{4}$", year_pub):
        raise ValueError("Year is invalid")

    # Quantity: Must be integers
    if not re.search(r"^\d+$", quantity):
        raise TypeError("Quantity must be an integer")

    # Quantity: Must be between 0 and 1000
    if not 0 <= int(quantity) <= 1000:
        raise ValueError("Quantity is invalid")

    # Cost: Must be a floating point value with 2 decimal places
    if not re.search(r"^\d+\.\d{2}$", cost_cad):
        raise ValueError("Cost is invalid")


def calculate_per_book_cost_cad(cost_cad, quantity):
    """
    This function calculates the per book cost of the order
    :param cost_cad: Total price of order in Canadian dollars, float
    :param quantity: Number of books in order, int
    """

    output = cost_cad / quantity

    return output


def write_book_order_details(filename, title, author, isbn, year_pub, quantity, cost_cad, unit_cost_cad):
    """
    This function will create a file with the given filename and fills the content with the details fiven
    :param filename: Name of the file to be created, str
    :param title: Title of the book, str
    :param author: Author of the book, str
    :param isbn: ISBN of the book, int
    :param year_pub: Year the book was published, int
    :param quantity: Number of books purchased, int
    :param cost_cad: Total rice of order, float
    :param unit_cost_cad: Price of one book, float
    """
    filename = filename+'.txt'

    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            file.write(
                f'BOOK ORDER\n'
                f'title={title}\n'
                f'author={author}\n'
                f'isbn={isbn}\n'
                f'year_pub={year_pub}\n'
                f'quantity={quantity}\n'
                f'cost_cad={cost_cad}\n'
                f'unit_cost_cad={unit_cost_cad}\n'
            )
    else:
        raise ValueError("Order file name already exists!")


def main():
    """
    This should not be called
    """

    pass


if __name__ == "__main__":
    main()
