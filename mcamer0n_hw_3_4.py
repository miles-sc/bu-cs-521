# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/22/24
# Homework Problem # 3_4
# Description of Problem: This problem reads and cleans every word from a
#                         text file and finds the longest word(s) and their
#                         length.

#Import libraries
import os
import string

#Set directory to the directory of the script currently being run
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

#Set filename constant and read
FILENAME="cs521_assign3_4.txt"

try:
      text_file=open(FILENAME,"r")
except:
      print("File does not exist! Check name/file path.")
      exit()

#Read file into list of words
word_list=text_file.read().split()

#Initialize valiables for length comparisons and cleaning
longest_length=0
longest_words=set()
punctuation=string.punctuation

#For loop to examine and clean every word from file
for i, word in enumerate(word_list):
      cleaned_word=""

      #For loop to clean punctuation and case
      for char in word:
            if char not in punctuation:
                  cleaned_word+=char.lower()

      #Replace original with cleaned word (not strictly needed)
      word_list[i]=cleaned_word

      #Sole new longest word case
      if len(cleaned_word)>longest_length:
            longest_words={cleaned_word,}
            longest_length=len(cleaned_word)

      #Tie for longest word case
      elif len(cleaned_word)==longest_length:
            longest_words.add(cleaned_word)

#Format longest word(s) for printing
formatted_words=""
for word in longest_words:
      formatted_words+=(word+", ")
formatted_words=formatted_words[:len(formatted_words)-2]

#Output for sole longest word
if len(longest_words)==1:
      print(f"The longest word in {FILENAME} is {formatted_words}"+\
            f" at {longest_length} words long.")

#Output for multiple longest words
else:
      print(f"The longest words in {FILENAME} are {formatted_words}"+\
            f" at {longest_length} words long.")
