# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/29/24
# Homework Problem # 4_4
# Description of Problem: This script analyzes a constant dictionary and
#                         prints its contents in a variety of formats

#Constant dictionary entry
MY_DICT = {'a':15, 'c':18, 'b':20}

#Calculate and print all the keys as a list
keys_list=list(MY_DICT.keys())
print(f'Keys: {keys_list}')

#Calculate and print all the values as formatted comma separated data
values_list=list(MY_DICT.values())
print('Values:',end=' ')
for i, value in enumerate(values_list):
    if i==(len(values_list)-1):
        print(value)
    else:
        print(value,end=', ')

#Print all the keys and values pairs as formatted data
print('Key value pairs:',end=' ')
keys_copy=keys_list.copy()
while len(keys_copy)>0:
    print(f'{keys_copy[0]}: {MY_DICT[keys_copy[0]]}', end='')
    if len(keys_copy)==1:
        print('')
    else:
        print(', ',end='')
    keys_copy.remove(keys_copy[0])

#Print a list of tuples for all the keys and values pairs, ascending by key
sorted_keys=sorted(keys_list)
d_list=[(key, MY_DICT[key]) for key in sorted_keys]
print(f'Key value pairs ordered by key: {d_list}')

#Print as formatted data all the keys and values pairs, ascending by value
reverse_dict=dict([(value, key) for (key, value) in MY_DICT.items()])
sorted_values=sorted(values_list)

e_string="Key value pairs ordered by value: "
for value in sorted_values:
    e_string+=f'{reverse_dict[value]}: {value}, '
e_string=e_string[:len(e_string)-2]
print(e_string)
