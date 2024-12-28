# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 10/6/24
# Homework Problem # 5_4
# Description of Problem: This program prompts the user for a filename, and
#                         upon successful reading of the file, prints a list
#                         of all words that occur exactly twice in the file.

import os
import string

#Function definition
def list_to_twice_words(word_list):
    '''
    list_to_twice_words() takes a list as an argument and returns a list that
    contains only words that occurred exactly TWICE in the original list.
    '''
    return list({word for word in word_list if word_list.count(word)==2})

#Main code block
if __name__=='__main__':

    # Set directory to the directory of the script currently being run
    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)

    # Loop until valid file name is obtained
    while True:

        filename=input('Enter a text file: ')

        try:
                text_file=open(filename,"r")
                text_string=text_file.read().lower()
                text_file.close()

        except:
            print('File does not exist or cannot be processed.')

        else:
            break

    #Set up to remove puctuation
    punc_trans=str.maketrans(string.punctuation," "*len(string.punctuation))

    #Remove punctuation, split into list of words, and run list_to_twice_words
    twice_list=list_to_twice_words(text_string.translate(punc_trans).split())

    #Print outputs
    print(f'The words in the file that appear exactly twice are: {twice_list}')
