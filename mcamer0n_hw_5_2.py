# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 10/6/24
# Homework Problem # 5_2
# Description of Problem: This script examines a constant prase and prints
#                         a variety of interesting information regarding the
#                         number of times each letter occurs.

# This program contains code adapted from my own work in HW 4_2 and 4_4

import string as st

# Letter Counts Function
def letter_counts(string):
    '''
    letter_counts() takes a string as its argument and returns a dictionary
    with the letters as keys and frequency counts as values.
    '''
    count_dict={}

    non_letters=st.punctuation+st.whitespace

    #Iterate through alphebetized phrase
    for i in sorted(string.upper()):

        #Filter out punctuation and whitespace
        if i not in non_letters:

            #Add to occurance count if letter has already been seen
            if i in count_dict:
                count_dict[i]+=1

            #Create new entry if the letter hasn't yet been seen
            else:
                count_dict[i]=1

    return count_dict

# Most Common Letter Function
def most_common_letter(string):
    '''
    most_common_letter() takes a string as its argument and returns a list
    of the most common letter(s).
    '''

    #Initialize
    max_occurrances=0
    frequent_letters=[]

    #Iterate through dictionary of letters and occurrance counts
    for letter, count in list(letter_counts(string).items()):

            #Sole new leader case
            if count>max_occurrances:
                frequent_letters=[letter]
                max_occurrances=count

            #Tie for lead case
            elif count==max_occurrances:
                frequent_letters.append(letter)

    return frequent_letters

# Histogram List Function
def string_count_histogram(string):
    '''
    string_count_histogram() takes a string as its argument and returns a list
    of the unique letters, with each letter being the repeated number of times
    it appears in the string. This list will then be printed one element per
    line (as a histogram).
    '''

    #List comprehension through dictionary items to create histogram data
    return [letter*count for letter, count in \
               list(letter_counts(string).items())]

# Main code block
if __name__=='__main__':

    PHRASE='A sword-day, a red day, ere the sun rises!'

    #LINE 0
    print(f'The string being analyzed is: "{PHRASE}"')

    #LINE 1
    line1='1. Letter counts: '

    count_dict=letter_counts(PHRASE)
    sorted_letters=sorted(count_dict.keys())

    for letter in sorted_letters:
        line1+=f"'{letter}': {count_dict[letter]}, "
    line1=line1[:len(line1)-2]

    print(line1)

    #LINE 2
    frequent_letter_list=most_common_letter(PHRASE)

    #Setting output according to number of most common letters

    #Sole leader case
    if len(frequent_letter_list)==1:
        appear='appears'
        letter='letter'
        frequent_letter_string=f"'{frequent_letter_list[0]}'"

    #Multiple leaders case
    else:
        appear='each appear'
        letter='letters:'
        frequent_letter_string=""
        for c in frequent_letter_list:
            frequent_letter_string+=f"'{c}', "
        frequent_letter_string=\
                        frequent_letter_string[:len(frequent_letter_string)-2]

    #Print statement
    print(f'2. Most frequent {letter} {frequent_letter_string} {appear}'+\
          f' {count_dict[frequent_letter_list[0]]} times.')

    #LINE 3
    hist_string='3. Histogram:'
    hist_list=string_count_histogram(PHRASE)
    for bar in hist_list:
        hist_string+=f"\n   {bar}"
    print(hist_string)
