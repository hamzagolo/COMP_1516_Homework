# Author: Marvin Neoh
# Date:
import login


def main():
    """
    Prompts the user to enter their first name, last name and BCIT ID to generate a default password, then asks the user
    to change it.
    """

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    bcit_id = input("Enter your BCIT ID: ")

    login.generate_password(first_name, last_name, bcit_id)
    login.change_password()


if __name__ == "__main__":
    main()
