# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 10/6/24
# Homework Problem # 5_1
# Description of Problem: This script asks the user for a filename and counts
#                         the number of vowels and consonants in the file if
#                         the filename is valid and exists in the same
#                         directory as the script.

# This program contains code adapted from my own work in HW 3_4

import os

# Define counter function
def vc_counter(filename):
    '''
    vc_counter() takes a valid file name (string) and returns a dictionary
    containing the number of consonants and vowels therein using "vowels"
    and "consonants" as keynames.
    '''

    # Open, read, and close file.
    text_file=open(filename,"r")
    text_string=text_file.read().upper()
    text_file.close()

    # Define vowels and consonants
    vowles=tuple('AEIOU')
    consonants=tuple('BCDFGHJKLMNPQRSTVWXYZ')

    # Iterate through text and count v/c matches
    v_count=sum((1 for char in text_string if char in vowles))
    c_count=sum((1 for char in text_string if char in consonants))

    # Create dictionary and return it
    return {'vowels':v_count,'consonants':c_count}


# Main code block
if __name__ == '__main__':

    # Set directory to the directory of the script currently being run
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)

    # Loop until valid name is obtained
    while True:

        filename=input('Enter a text file: ')

        try:
            text_file=open(filename,"r")
            text_file.close()
        except:
            print('File does not exist or cannot be opened.')
        else:
            break

    # Run counter function with verified user input
    count_dict=vc_counter(filename)

    # Print results
    print(f'Total # of vowels in text file: {count_dict["vowels"]}')
    print(f'Total # of consonants in text file: {count_dict["consonants"]}')
