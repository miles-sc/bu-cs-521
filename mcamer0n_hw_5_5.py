# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 10/6/24
# Homework Problem # 5_5
# Description of Problem: This script asks the user for an integer for a
#                         factorial and then calculates the factorial with and
#                         without recursion before printing the results.

#Recursive factorial function definition
def factorial(num):
    '''
    factorial() takes an integer as its argument and returns its factorial
    using recursion
    '''
    #0 and 1 case - stop recursion
    if num<2:
        return 1

    #For positive numbers greater than 1, call function again
    else:
        return num*factorial(num-1)

#Non-recursive factorial function definition
def factorial2(num):
    '''
    factorial2() takes an integer as its argument and returns its factorial
    without using recursion
    '''
    #Use for loop to multiply numbers between 1 and num
    product=1
    for i in range (1,num+1):
        product*=i
    return product



#Main code block
if __name__=='__main__':

    #Loop until valid input obtained
    while True:
        user_input=input("Enter a starting integer for a factorial: ")

        try:
            #TypeError can occur here
            num=int(user_input)

        except:
            print("The input was not a valid integer.")

        else:
            #Test for negative numbers (not allowed)
            if num>=0:
                break
            else:
                print("Negative integers are not allowed for factorials.")

    #Print outputs
    print(f'Factorial of {num:,} using recursion: {factorial(num):,}')
    print(f'Factorial of {num:,} without using recursion: {factorial2(num):,}')
