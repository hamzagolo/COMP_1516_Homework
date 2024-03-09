# Author: Marvin Neoh
import re


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
    if not re.search(r"\d+", order_num):
        raise ValueError("Order Number is invalid.")

    if not re.search(r"[A-Za-z\s]+", title):
        raise ValueError("Title is invalid.")

    if not re.search(r"[A-Za-z\s']+", author):
        raise ValueError("Author is invalid.")

    if not re.search(r"^\d+$", isbn):
        raise ValueError("ISBN must be an integer.")

    if not re.search(r"^\d+{4,20}$", title):
        raise ValueError("Title is invalid.")


def calculate_per_book_cost_cad(cost_cad, quantity):
    """
    This function calculates the per book cost of the order
    :param cost_cad: Total price of order in Canadian dollars, float
    :param quantity: Number of books in order, int
    """
    pass


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
    pass

def main():
    """
    This should not be called
    """
    pass


if __name__ == "__main__":
    main()