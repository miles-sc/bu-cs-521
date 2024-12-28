# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 10/6/24
# Homework Problem # 5_3
# Description of Problem: This script takes a string from the user containing
#                         4 delimited numbers, tests for a variety of errors
#                         and issues, performs some arithmetic with the
#                         numbers, and prints the results.

#Main code block
if __name__=='__main__':

    #Loop until valid input is achieved
    while True:

        i_string=input("Please enter 4 numbers delimited by the letter"+\
                           " v (e.g. 1v2v3v4): ")

        try:
            #ValueError can occur here
            i_list=[float(num) for num in i_string.split("v")]

            #Check to make sure list isn't too long
            if len(i_list)<5:
                #ZeroDivisionError OR Index Error can occur here
                result = ((i_list[0]*i_list[1])+i_list[2])/i_list[3]
                break
            #I would prefer to make the above block read "if len(i_list)==4"
            #But I left it at <5 so ValueError would be possible in the
            #following line for the sake of the asssignment.

            else:
                print("The input contained too many delimited numbers.")

        except ValueError:
            print("The values between the delimiters were not valid numbers,"+\
                  " or the wrong delimiter was used.")

        except ZeroDivisionError:
            print("The fourth value cannot be 0. It is used as a divisor.")

        except IndexError:
            print("The input contained too few numbers.")


    #Print outputs
    print(f'({i_list[0]}*{i_list[1]}+{i_list[2]})/{i_list[3]}={result}')
