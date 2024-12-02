# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/14/24
# Homework Problem # 2_5
# Description of Problem: This problem requires printing a string according to
#                         a number's divisibility by 2, 3, and/or 5 for all
#                         numbers from 1 to 30.

maxval=30

for i in range(maxval):
    x=i+1
    d2=""
    d3=""
    d5=""

    if x%2==0:
        d2="two"

    if x%3==0:
        d3="three"

    if x%5==0:
        d5="five"

    print(str(x)+": "+d2+d3+d5)

print("--------------------")
