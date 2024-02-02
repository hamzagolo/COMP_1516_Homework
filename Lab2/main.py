import utilities as util


def main():

    radius_of_circle = input("Enter the radius of a circle in cm: ")
    print("The area of the circle is ", util.calculate_circle_area(radius_of_circle))

    radius_of_sphere = input("Enter the radius of a sphere in cm: ")
    print("The volume of the sphere is:", util.calculate_sphere_volume(radius_of_sphere))

    print("The Body Mass Index is", util.calculate_bmi())

    print("The hypotenuse length of the right triangle is:", util.calculate_hypotenuse())


if __name__ == '__main__':
    main()
