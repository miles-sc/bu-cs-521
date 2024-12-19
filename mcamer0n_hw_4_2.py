# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/29/24
# Homework Problem # 4_2
# Description of Problem: This script examines a constant prase and records
#                         the number of occurrances of each letter in a
#                         dictionary. It reports the most common letters(s)
#                         and how many times they/it occurred.

#Import library, initialize contant and variables
import string

PHRASE='A sword-day, a red day, ere the sun rises!'

count_dict={}

non_letters=string.punctuation+string.whitespace

max_occurrances=0
frequent_letters=set()

#Iterate through alphebetized phrase
for i in sorted(PHRASE.upper()):

    #Filter out punctuation and whitespace
    if i not in non_letters:

        #Add to occurance count if letter has already been seen
        if i in count_dict:
            count_dict[i]+=1

        #Create new entry if the letter hasn't yet been seen
        else:
            count_dict[i]=1

        #Keep track of most common words:

        #Sole new leader case
        if count_dict[i]>max_occurrances:
            frequent_letters={i,}
            max_occurrances=count_dict[i]

        #Tie for lead case
        elif count_dict[i]==max_occurrances:
            frequent_letters.add(i)


#Print outputs
print(f'The string being analyzed is: "{PHRASE}"')
print(f'1. Dictionary of letter counts: {(count_dict)}')

#Setting output according to number of most common letters
if len(frequent_letters)==1:
    appear='appears'
    letter='letter'
    frequent_letters='"'+frequent_letters.pop()+'"'
else:
    appear='appear'
    letter='letters'
    frequent_letters=sorted(frequent_letters)


print(f'2. Most frequent {letter} {frequent_letters} {appear}'+\
      f' {max_occurrances} times.')
