# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/14/24
# Homework Problem # 2_3
# Description of Problem: This problem requires taking two numbers from the
#                         user and presenting the quotient in both decimal
#                         and remainder formats.

#Collect user inputs and cast
x=int(input("Please enter integer #1: "))
y=int(input("Please enter integer #2: "))

#Print outputs
print(str(x)+" divided by "+str(y)+" is:")
print("    "+str(round((x/y),2))+" as a floating-point value")
print("    "+str(int(x//y))+" remainder "+str(int(x%y)))
