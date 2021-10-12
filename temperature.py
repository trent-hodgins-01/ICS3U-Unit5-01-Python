# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/12/2021
# This is the temperature program
# The user enters in the temperature in celsius
# The program displays the temperature in Fahrenheit


def celsius_to_fahrenheit():
    # calculates celsius to fahrenheit

    # input
    celsius_as_string = input("Enter in the temperature(Celsius): ")

    # process
    try:
        celsius_as_number = int(celsius_as_string)
        fahrenheit = (9 / 5) * celsius_as_number + 32

        # output
        print("It is {0}° Fahrenheit".format(fahrenheit))

    except Exception:
        print("Invalid input")


def main():
    # this function just calls other functions

    # call functions
    celsius_to_fahrenheit()


if __name__ == "__main__":
    main()
