# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/14/24
# Homework Problem # 2_4
# Description of Problem: This problem requires getting a length and height
#                         from the user and calculating the area of a square,
#                         rectangle, and triangle using those parameters.

#Collect user length and height and cast as float
length=float(input("Enter a length in decimal form: "))
height=float(input("Enter a height in decimal form: "))

#Repeat back the inputs to the user
print("You entered a length of "+str(length)+" and a height of "\
      +str(height)+".")

#Calculate and print the appropriate areas
print("Your shapes and there areas are:")
print("    Square: "+f"{(length*length):.2f}")
print("    Rectangle: "+f"{(length*height):.2f}")
print("    Triangle: "+f"{(length*height*0.5):.2f}")
