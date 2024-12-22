# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/29/24
# Homework Problem # 4_5
# Description of Problem: This script requests a user input and tests that it
#                         is a valid nuber that does not contain commas. If
#                         that is true, it prints the inputted number as text
#                         using a constant dictionary.

#Set constant dictionary
DICT={'1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six',\
      '7':'Seven','8':'Eight','9':'Nine','0':'Zero','-':'Negative',\
      '.':'Point'}

#Infinite loop until agreeable input is given
while True:

    #Ask for user input and convert to more useful list of characters
    user_num=input('Enter a number: ')
    num_list=list(user_num)

    #Check for commas and remove them if present, create cleaned string
    commas=False
    if ',' in num_list:
        commas=True
        num_string=''.join([char for char in num_list if char!=','])
    else:
        num_string=''.join(num_list)


    #Check if the cleaned string can be converted to a float type
    try:
        num_float=float(num_string)
        numeric=True
    except:
        numeric=False

    #Error message for non numeric input
    if not numeric:
        print(f'"{user_num}" is not a valid number. Please try again')

    #Error message for numeric input that contains commas
    elif commas:
        print('Please try again without entering commas.')

    #Print output for valid entry, and break for infinite loop
    else:
        print('As Text: ',end='')
        for digit in num_list:
            print(DICT[digit],end=" ")
        break
