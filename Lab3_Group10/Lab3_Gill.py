# Filename: Lab3_Gill
# Name: Dylan Gill
# Date: February 29th, 2024
# Description: Calculate the area of shapes.

# Imports
import math

# Functions to get the area of a circle, trapezium, ellipse, rhombus.
def circle_area():
    r = float(input("\nEnter the radius of the circle: "))
    circleA =  math.pi * (r ** 2)
    print("The area of the circle is: ", round(circleA, 2))

def trapezium_area():
    a = float(input("\nEnter the length of base 1 of the trapezium: "))
    b = float(input("Enter the length of the base 2 of the trapezium: "))
    h = float(input("Enter the height of the trapezium: "))
    trapA = 0.5 * (a + b) * h
    print("The area of the trapezium is: ", round(trapA, 2))

def ellipse_area():
    a = float(input("\nEnter the length of axis (a) of the ellipse: "))
    b = float(input("Enter the length of the axis (b) of the ellipse: "))
    ellipseA = math.pi * a * b
    print("The area of the ellipse is: ", round(ellipseA, 2))

def rhombus_area():
    d1 = float(input("\nEnter the length of the first diagonal of the rhombus: "))
    d2 = float(input("Enter the length of the second diagonal of the rhombus: "))
    rhombusA = (d1 * d2) / 2
    print("The area of the rhombus is: ", round(rhombusA, 2))

# Function for calculate menu
def calculate_menu():
    print("\n=========================================")
    print("Please enter one of the following options:")
    print("- 'c' to calculate the area of a Circle")
    print("- 't' to calculate the area of a Trapezium")
    print("- 'e' to calculate the area of a Ellipse")
    print("- 'r' to calculate the area of a Rhombus")
    print("- 'q' to quit the program...")
    print("=========================================")

if __name__ == "__main__":
    exit_flag = False
    while not exit_flag:
        calculate_menu()
        userInput = input("Enter which shape you want to calculate: ").lower()

        if userInput == 'c':
            circle_area()
        elif userInput == 't':
            trapezium_area()
        elif userInput == 'e':
            ellipse_area()
        elif userInput == 'r':
            rhombus_area()
        elif userInput == 'q':
            print("\nQuitting the program... Goodbye!")
            exit_flag = True
        else:
            print("\n!ERROR! Please enter a valid option.")
