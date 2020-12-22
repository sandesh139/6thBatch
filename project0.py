# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#print("Whats up python!")
# importing calendar module
import calendar
import sys
#import os
import os
# Program make a simple calculator
# This function adds two numbers


def add(x, y):
    return x + y
# This function subtracts two numbers


def subtract(x, y):
    return x - y
# This function multiplies two numbers


def multiply(x, y):
    return x * y
# This function divides two numbers


def divide(x, y):
    return x / y

# A reusable function that takes a list of app,
# prints the name as well as
# returns the number from 1 to the length of the list as a screening


def choose_one(list_screening):
    list_length = len(list_screening)

    # print how many applications we have
    print(f"We have {list_length} options for you:")

    # print the name of application using for loop
    for i in range(list_length):
        print(f'{i+1}. {list_screening[i]}')

    while(True):
        app = int(
            input(f"Select one option from above: (1 - {list_length}): "))
        if (app <= list_length) and (app > 0):
            return app
        else:
            print(
                f"Wrong choice choose between (1 to {list_length}) or press ctrl+c to exit: ")

# passing the application screening as a function


def app_screening():
    list_apps = ["Calculator",
                 "Calendar",
                 "Temperature converter -- Still in construction",
                 "distance converter",
                 "weight converter -- Still in construction",
                 "data size converter -- Still in construction",
                 "currency converter -- Still in construction",
                 "date converter -- Still in construction"]

    app = choose_one(list_apps)
    os.system("clear")
    return app, list_apps[app-1]


def distance_screening():
    print("Please Select one operation from below:")

    list_distance_screening = ["KiloMeter to Meter",
                               "Meter to KiloMeter",
                               "Kilometer to Mile",
                               "Mile to Kilometer",
                               "Meter to Mile",
                               "Mile to Meter",
                               "Foot to meter",
                               "Meter to Foot",
                               "Foot to Inch",
                               "Inch to Foot"
                               ]

    choice = choose_one(list_distance_screening)
    os.system("clear")
    return choice, list_distance_screening[choice-1]

# takes the app name and prints general questioning for returning the input


def distance_printing(app_name, app_convert):
    os.system("clear")
    print(f'You choosed {app_name}: ')
    converting = float(input(f"Enter the distance in {app_convert}: "))
    return converting


def calculator_app():
    print("Please Select one operation from below:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = input("Enter choice(1/2/3/4): ")
    os.system("clear")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("wrong choice try again or press ctrl+c to close")
        main()


def calendar_app():
    # To take month and year input from the user
    yy = int(input("Enter year: "))
    mm = int(input("Enter month: "))

    # display the calendar
    print("\n")
    print(calendar.month(yy, mm))


def distance_app():
    # performs the screening of the app and get back the choice and the name
    choice, app_name = distance_screening()

    # clearing the screen
    os.system("clear")

    """
    Used split() function for the converting app name to list for generalization
    
    For eg : (Kilometer to meter) change to:

    app_convert[0] = kilometer
    app_convert[1] = to (usually it is not needed)
    app_convert[2] = meter

    It gives an ability to use print as a general form
    """
    app_convert = app_name.split()

    distance = distance_printing(app_name, app_convert[0])

    # kilometer to meter
    if choice == 1:
        converted = distance*1000

    # Meter to kilometer
    elif choice == 2:
        converted = distance/1000

    # Km to mile
    elif choice == 3:
        converted = distance / 1.61

    # mile to KM
    elif choice == 4:
        converted = distance * 1.61

    # meter to mile
    elif choice == 5:
        converted = distance / 1609

    # Mile to meter
    elif choice == 6:
        converted = distance * 1609

    # Foot to meter
    elif choice == 7:
        converted = distance / 3.281

    # meter to foot
    elif choice == 8:
        converted = distance * 3.281

    # Foot to Inch
    elif choice == 9:
        converted = distance * 12

    # Inch to foot
    else:
        converted = distance / 12

    print(
        f"{distance} {app_convert[0]} is {round(converted,4)} {app_convert[2]}.")


# main function. Program starts from here
def main():
    try:
        # returning 1 through the number of last app
        app, app_names = app_screening()
        os.system("clear")

        print(f'Thanks for choosing {app_names}')

        if app == 1:
            calculator_app()
        elif app == 2:
            calendar_app()

        # If they choose distance converter
        elif app == 4:
            distance_app()

        else:
            print(f"\nSorry, The app {app} is still on construction. Try again or press ctrl+c to exit\n")
            main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except:
        os.system("clear")
        print("Something is wrong please try again. Please include numeric value only or press ctrl+C to end the app")
        main()


if __name__ == "__main__":
    main()
