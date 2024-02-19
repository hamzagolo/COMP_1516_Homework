# Author: Marvin Neoh
import math


def get_square_numbers_between(first, last):
    """
    This function creates and returns a list of all the square numbers between the two inputted numbers.
    :param first: Number, int
    :param last: Number, int
    :return: List of numbers, list
    """
    output = []

    # square root the first and last number to get the closest whole number, then start incrementing from there
    first_root, last_root = math.ceil(math.sqrt(int(first))), math.floor(math.sqrt(int(last)))

    for number in range(first_root, last_root+1):
        output.append(number**2)

    return output


def process_user_input():
    """
    This function shows the sum, minimum and maximum numbers entered by the user.
    :return:
    """
    output = []
    not_zero = True

    while not_zero:
        number = input("Enter a number, or enter 0 to end: ")
        if number != '0':
            output.append(number)
        else:
            not_zero = False

    max_num = min_num = sum_num = int(output[0])

    for number in output[1:]:

        number = int(number)

        sum_num += number

        if number > max_num:
            max_num = number

        elif number < min_num:
            min_num = number

    print(f"Your numbers are: {output}")
    print(f"The sum is {sum_num}")
    print(f"The min is {min_num}")
    print(f"The max is {max_num}")


def main():
    """
    This function calls the get_square_numbers_between() and process_user_input() functions
    :return:
    """
    first_number = input('Enter your first number: ')
    second_number = input('Enter your second number: ')
    #get_square_numbers_between(first_number, second_number)
    print(get_square_numbers_between(first_number, second_number))

    process_user_input()


if __name__ == "__main__":
    main()
