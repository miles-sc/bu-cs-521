# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/22/24
# Homework Problem # 3_5
# Description of Problem: This problem requires estimating the odds that two
#                         people in a group will share a birthday, given a
#                         certain number of people per group and
#                         certain sample size for the estimate

#Import libraries
import random

#Set constants and initialize match count
TESTS=50
SIZE=30

matches=0

#For loop to iterate through given number of tests
for i in range(TESTS):

    #Creation of test with given number of people with random birthdays
    test=[random.randint(1,365) for j in range(SIZE)]

    #Test for duplicates by converting list to set
    if len(set(test)) != 30:
        matches+=1

#Calculate percentate
percentage=100*matches/TESTS

#Print output
print(f"In {TESTS} groups of {SIZE} people, {matches} groups had at least"+\
      f" one birthday match.\nThis is {percentage}%.")
