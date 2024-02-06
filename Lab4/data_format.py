# Author: Marvin Neoh
# Date:

def get_book_info():
    """
    This function
    :return:
    """
    book_title = input("Enter book title: ").strip()
    book_isbn = input("Enter ISBN: ").strip()
    book_author_last_name = input("Enter author last name: ").strip()
    book_publisher = input("Enter book publisher: ").strip()
    year_published = input("Enter year published: ")
    book_price_usd = input("Enter book in US Dollars: ")

    book_info = f'{book_title}/{book_isbn}/{book_author_last_name}/{book_publisher}/{year_published}/{float(book_price_usd):.2f}'

    return book_info


def to_csv_format(book_info):
    """
    Takes book info as input and returns it in CSV format
    :param book_info: Relevant book information, str
    :return:
    """

    pass


def to_json_format(book_info):
    """
    Takes book_info as input and returns it in JSON format
    :param book_info:
    :return:
    """

    pass


def main():
    """

    :return:
    """

    book_info = get_book_info()
    # print(book_info)
   # print(to_csv_format(book_info))
   # print(to_json_format(book_info))


if __name__ == "__main__":
    main()
