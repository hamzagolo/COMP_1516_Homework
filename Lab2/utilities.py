import math


def calculate_circle_area(radius):
    """
    Calculates the area of a circle given the radius
    :param radius: radius of a circle, float
    :return: the area of the circle, which is calculated using the formula pi*r^2
    """
    circle_area = math.pi * (float(radius)**2)

    return circle_area


def calculate_sphere_volume(radius):
    """
    Calculates  the volume of a sphere given the radius
    :param radius: radius of a sphere, float
    :return: the volume of teh sphere, calculated using the formula 4/3*pi*r^3
    """
    sphere_volume = (4/3) * math.pi * (float(radius)**3)

    return sphere_volume


def calculate_bmi():
    """
    Calculates the Body Mass Index using inputted weight in kilograms and height in emters
    :return: the Body Mass Index which is calculated using the formula weight/(height*height)
    """
    weight_kilogram = float(input("Enter your weight in kilograms: "))
    height_meter = float(input("Enter your height in meters: "))

    body_mass_index = weight_kilogram / (height_meter**2)

    return body_mass_index


def calculate_hypotenuse():
    """
    Calculate the hypotenuse of a right triangle given two sides, a and b
    :return: the hypotenuse of the triangle, utilizing the hypot() function from the module math
    """
    length_side_a_cm = float(input("Enter the length of side A in cm: "))
    length_side_b_cm = float(input("Enter the length of side B in cm: "))

    hypotenuse = math.hypot(length_side_a_cm, length_side_b_cm)

    return hypotenuse
