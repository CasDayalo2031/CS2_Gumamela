# Distance Program Calculator

## Description
Calculates the distance between two points (x1, y1) and (x2, y2) on a 2D plane

## How to Run 
1. Open the program file in VS Code, Replit, or Google Colab
2. Run the program
3. Enter the values for x1, y1, x2, y2
4. Check the distance displayed

## Input Needed
- x1
- y1
- x2
- y2

## Sample Output
Enter x1: 4
Enter y1: 8
Enter x2: 5
Enter y2: 9
The distance is:  1.4142135623730951 (❁´◡`❁)

## Author
Name: Dayalo, Chloe Anne
Section: Gumamela



import math

# Asks the user to enter the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
# Asks the user to enter the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Computing the distance using the distance formula
A = pow(x2 - x1, 2)
B = pow(y2 - y1, 2)
answer = A + B
distance = math.sqrt(answer)

# Displays the result to the user
print ("The distance is: ", distance, "(❁´◡`❁)")
