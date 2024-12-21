# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/29/24
# Homework Problem # 4_3
# Description of Problem: This script merges a list of first names and a list
#                         of last names into a dictionary with last names as
#                         keys. There must be more last names than firsts.

#Set constants
FIRST_NAMES=['Jane', 'John']
LAST_NAMES=['Doe', 'Deer', 'Black']

#Print error and message if there are more first names than last names
if len(FIRST_NAMES)>len(LAST_NAMES):
    print("Error: There cannot be more first names than last names.")
    exit()

#Create a copy of FIRST_NAMES and add None values to match LAST_NAME's length
first_names_copy=FIRST_NAMES.copy()

while len(first_names_copy)<len(LAST_NAMES):
    first_names_copy.append(None)

#Zip up the lists to create the dictionary
name_dict=dict(zip(LAST_NAMES,first_names_copy))

#Print outputs
print(f"First names: {FIRST_NAMES}\n"+
      f"Last names: {LAST_NAMES}\n"+
      f"Name Dictionary: {name_dict}")
