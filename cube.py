# Get math equations
import math


# define main
def main():

    # intro
    print("I calculate the area and volume of cubes")

    # get edge
    print("what is the edge size?: ")
    edge = float(input())

    # calculate area
    area = 6 * (edge**2)

    # calculate volume
    volume = edge**3

    # print area and volume
    print("The area is:{}cm^2".format(area))
    print("The volume is: {}cm^3".format(volume))


if __name__ == "__main__":
    main()
