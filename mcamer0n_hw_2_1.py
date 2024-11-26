# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/14/24
# Homework Problem # 2_1
# Description of Problem: This problem requires asking for two integers from
#                         the user, finding their product, converting it to
#                         different formats, and printing outputs.

#Collect user inputs and cast to integer type
x=int(input("Please enter integer #1: "))
y=int(input("Please enter integer #2: "))

#Caluclate product and converted formats
z=x*y
z_bin=bin(z)
z_oct=oct(z)
z_hex=hex(z)

#Print outputs
print("Integer #1 is "+str(x)+". Integer #2 is "+str(y)+ \
      ". Their product is "+str(z)+".")
print("The product can be expressed in the following ways:")
print("    Binary: "+str(z_bin))
print("    Octal: "+str(z_oct))
print("    Decimal: "+str(z))
print("    Hexadecimal: "+str(z_hex))
