# Author: Marvin Neoh
# Date:


def generate_password(first_name, last_name, bcit_id):
    """
    Generates the default login password given the inputs
    :param first_name: First name of user, str
    :param last_name: Last name of user, str
    :param bcit_id: BCIT identification number, str
    :return:
    """

    first_name_process = first_name.capitalize()
    last_name_process = last_name.capitalize()

    if len(first_name_process) > 3:
        first_name_process = first_name_process[:3]

    if len(last_name_process) > 3:
        last_name_process = last_name_process[:3]

    if len(bcit_id) > 3:
        bcit_id = bcit_id[-3:]

    # password = f'{first_name_process}{last_name_process}{bcit_id}'

    print(f"Your login is {first_name_process}{last_name_process}{bcit_id}")


def change_password():
    """
    Prompts the user to enter a new password and checks if it meets the specifications
    :return: Does not return anything
    """

    specifications_met = False

    while not specifications_met:

        password = input('Enter new password: ')

        if not no_special_characters(password):
            print('Password should not contain any special characters.')

        elif len(password) < 7:  # checks for the length requirement
            print('Password must have at least 7 characters.')

        elif password.isdigit():    # returns True if password only has numbers
            print("Password must have at least one alphabet.")

        elif password.isalpha():    # returns True if password only has alphabets
            print("Password must have at least one number.")

        elif password.isupper():    # returns True if password only has uppercase letters
            print("Password must have at least one lowercase character.")

        elif password.islower():    # returns True if password only has lowercase letters
            print("Password must have at least one uppercase character.")

        else:
            specifications_met = True
            print(f'Valid password. Your new password is: {password}')


def no_special_characters(password):
    """
    Checks if the password contains any special characters
    :param password: Password, str
    :return: True is there is no special characters or False if there is, bool
    """
    special_characters = [
        '\'', '\"', '@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '<', '>', '?', '/', '\\',
        '|', '{', '}', '`', '~', ':', '[', ']', '.', ',',
    ]

    for character in password:
        if character in special_characters:
            return False

    return True
