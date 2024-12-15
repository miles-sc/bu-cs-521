# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/22/24
# Homework Problem # 3_3
# Description of Problem: This problem requires printing out a numbered list
#                         of all of the items on a breakfast menu, and taking
#                         a valid order from the user.

#Input copied from assignment description
menu=["ham", "eggs", "bacon", "fish", "toast", "spam", "fruit"]

#Print menu with for loop using range() function
print("Time for breakfast! There are "+str(len(menu))+" items on the menu:")
for i in range(len(menu)):
    print("    "+str(i+1)+". "+menu[i])

#Set up while loop to ask for an order until a valid one is placed
order_acquired=False
while not order_acquired:

    #Collect and format order
    order=input("What would you like? ")
    order=order.lower()

    #Number order case
    if order.isnumeric() and 0<int(order)<(len(menu)+1):
        print(f"Your order of {menu[int(order)-1]} is coming right up!")
        order_acquired=True

    #String order case
    elif order in menu:
        print(f"Your order of {order} is coming right up!")
        order_acquired=True

    #Invalid order case
    else:
        print("We don't have that on the menu!")
