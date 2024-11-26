# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/14/24
# Homework Problem # 2_2
# Description of Problem: This problem requires printing out a numbered list
#                         of all of the items on a breakfast menu.

#Input copied from assignment description
menu = ["ham", "eggs", "bacon", "fish", "toast", "spam", "congee", "fruit"]

#Print menu with for loop using range() function
print("Time for breakfast! There are "+str(len(menu))+" items on the menu:")
for i in range(len(menu)):
    print("    "+str(i+1)+". "+menu[i])
