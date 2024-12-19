# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/29/24
# Homework Problem # 4_1
# Description of Problem: This problem requires establishing a list counting
#                         down from 55 to 5 by 10, and then generating a new
#                         list with each element as the sum of the
#                         corresponding element of the original list, plus its
#                         neighbors.

#Create constant list
LIST_A=list(range(55,4,-10))

#Initialize new list
list_b=[]

#Iterate through elements of constant list
for i, num in enumerate(LIST_A):

    #First element edge case
    if i==0:
        list_b.append(num+LIST_A[i+1])

    #Last element edge case
    elif i==(len(LIST_A)-1):
        list_b.append(num+LIST_A[i-1])

    #Middle/typical element standard case
    else:
        list_b.append(num+LIST_A[i-1]+LIST_A[i+1])

#Print outputs
print(f"Input list: {LIST_A}")
print(f"Output list: {list_b}")
