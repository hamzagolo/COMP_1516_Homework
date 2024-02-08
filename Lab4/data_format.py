# Author: Marvin Neoh
# Date:

def get_book_info():
    """
    This function prompts the user to get information for a book and returns the information compressed in one string
    :return: Book information, str
    """
    book_title = input("Enter book title: ").strip().title()
    book_isbn = input("Enter ISBN: ").strip()
    book_author_last_name = input("Enter author last name: ").strip().capitalize()
    book_publisher = input("Enter book publisher: ").strip().capitalize()
    year_published = input("Enter year published: ")
    book_price_usd = input("Enter book in US Dollars: ")

    book_info = (f'{book_title}/{book_isbn}/{book_author_last_name}/{book_publisher}/{year_published}/'
                 f'{float(book_price_usd):.2f}')

    return book_info


def to_csv_format(book_info):
    """
    Takes book info as input and returns it in CSV format
    :param book_info: Relevant book information, str
    :return: Book info in CSV format, str
    """

    return book_info.replace('/', ',')


def to_json_format(book_info):
    """
    Takes book_info as input and returns it in JSON format
    :param book_info: Relevant book information, str
    :return: Book info in JSON format, dict
    """

    book_info_split = book_info.split('/')

    output = {
        'title': book_info_split[0],
        'isbn': book_info_split[1],
        'author_last_name': book_info_split[2],
        'year_published': book_info_split[3],
        'price': book_info_split[4],
    }

    return output


def main():
    """
    Calls book_info to get information on a book, and passes it to be printed out in CSV and JSON formats.
    """

    book_info = get_book_info()

    print(to_csv_format(book_info))
    print(to_json_format(book_info))


if __name__ == "__main__":
    main()
