#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2023-1-10

#This program tells the users the surface area and volume of a cube.
def main():

    while True:
        try:
            # Ask the user for the side length of the cube
            side_length = float(input("Enter the side length of the cube: "))
            if side_length < 0:
                print("Enter Positive Number.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")

    # Ask the user for the measurement unit they would like to use
    measurement_unit = input("Enter the measurement unit (e.g. cm, m, in): ")

    # Calculate the surface area of the cube
    surface_area = 6 * side_length**2

    # Calculate the volume of the cube
    volume = side_length**3

    # calculate the sum of both volume and surface_area
    sum_of = surface_area + volume

    # Display the results with measurement unit
    print(f"Surface area of cube: {surface_area} {measurement_unit}^2")
    print(f"Volume of cube: {volume} {measurement_unit}^3")
    print(f"Sum of Volume and Surface Area of cube: {sum_of}")

    # Ask the user if they would also like to solve area and perimeter for a square.
    answer = input("Do you want to find area and perimeter of a square? (yes or no): ")

    # .lower is used in case the user spells it differently.
    if answer.lower() == "yes":
        side_length = side_length
        if side_length < 0:
            print("Enter Positive Integer, please try again.")
        else:
            area_of_square = side_length**2
            perimeter_of_square = 4 * side_length
            sum_of_2 = perimeter_of_square + area_of_square
            # Display the results with measurement unit
            print(f"Area of square: {area_of_square} {measurement_unit}^2")
            print(f"Perimeter of square: {perimeter_of_square} {measurement_unit}")
            print(f"The sum of area and perimeter is {sum_of_2}")
            print()
            print("Thank you for Playing!")
    else:
        print("Thank you for Playing!")


if __name__ == "__main__":
    main()

    # asks the user if they want to restart after the program has finished
    restart = int(input("Enter 1 if you'd like to restart: "))
    while restart == 1:
        main()
        restart = int(input("Enter 1 if you'd like to restart: "))
