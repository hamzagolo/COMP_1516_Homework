# Author: Marvin Neoh
import sys
import book_order_utils


def main():
    """
    This function verifies that there are exactly 8 command-line arguments
    :return:
    """
    order_num = sys.argv[1]
    title = sys.argv[2]
    author = sys.argv[3]
    isbn = sys.argv[4]
    year_pub = sys.argv[5]
    quantity = sys.argv[6]
    cost_in_canadian_dollars = sys.argv[7]

    try:
        book_order_utils.validate_book_order_details(order_num, title, author, isbn, year_pub, quantity,
                                                     cost_in_canadian_dollars)
        cost_per_unit = book_order_utils.calculate_per_book_cost_cad(float(cost_in_canadian_dollars), int(quantity))
        book_order_utils.write_book_order_details(order_num, title, author, isbn, year_pub, quantity,
                                                  cost_in_canadian_dollars, cost_per_unit)

    except ValueError as v:
        print(f"Value Error: {v}")

    except TypeError as t:
        print(f"Type Error: {t}")

    except ZeroDivisionError:
        print("No Books in Order")


if __name__ == "__main__":
    main()
