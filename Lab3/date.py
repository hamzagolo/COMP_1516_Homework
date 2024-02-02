# Marvin Neoh and Henry Motloch

def main():
    print(get_day_of_the_week(6, 6, 2118))
    print(is_leap_year(2023))
    print(is_leap_year(2024))


def get_day_of_the_week(month, day, year):
    """
    Returns the day of the date corresponding to given date
    :param month: month, int
    :param day: day, int
    :param year: year, int
    :return: Day of the week, str
    """
    # used for calculations
    month_code = {
        1: 1,
        2: 4,
        3: 4,
        4: 0,
        5: 2,
        6: 5,
        7: 0,
        8: 3,
        9: 6,
        10: 1,
        11: 4,
        12: 6,
    }

    # used to determine the day of the week
    day_of_the_week = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
    }

    # modifier for specific years
    special_offset_years = {
        1600: 6,
        1700: 4,
        1800: 2,
        2000: 6,
        2100: 4,
    }

    century = int(str(year)[:2])*100        # get the century
    shortened_year = int(str(year)[2:])     # get last two digits of the year
    how_many_12s = shortened_year//12       # divide shortened year by 12

    # makes sure % function doesn't return anything if the year is less than 12
    if shortened_year < 12:
        remainder = 0
    else:
        remainder = shortened_year % 12

    how_many_4s = remainder//4              #  divide remainder by 4
    magic_number = how_many_12s + remainder + how_many_4s + day + month_code[month]

    # special offset section
    if (month == 1 or month == 2) and is_leap_year(year):
        magic_number += 6
    if century in special_offset_years:
        magic_number += special_offset_years[century]


    return day_of_the_week[magic_number % 7]


def is_leap_year(year):
    """
    Returns True if the input is a leap year and False if it is not a leap year
    :param year: int
    :return: Boolean
    """

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
        else:
            return True

    return False


if __name__ == '__main__':
    main()
