# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/22/24
# Homework Problem # 3_2
# Description of Problem: This problem requires encoding a message using a
#                         "Caesar Cipher" and a given shift value.

#Establish constants and print original message
SHIFT=6
MESSAGE="A sword-day, a red day, ere the sun rises!"
print(f"The unencoded message is: {MESSAGE}")

#Initialize coded message
coded_message=""

#Iterate through each character in original message
for i in MESSAGE:

    #Standard capital letter conversions
    if (ord("A")-1)<ord(i)<(ord("Z")+1-SHIFT):
        coded_message+=chr(ord(i)+SHIFT)

    #End-of-alphabet capital letter conversions
    elif (ord("Z")-SHIFT)<ord(i)<(ord("Z")+1+SHIFT):
        coded_message+=chr(ord(i)-26+SHIFT)

    #Standard lowercase letter conversions
    elif (ord("a")-1)<ord(i)<(ord("z")+1-SHIFT):
        coded_message+=chr(ord(i)+SHIFT)

    #End-of-alphabet lowercase letter conversions
    elif (ord("z")-SHIFT)<ord(i)<(ord("z")+1+SHIFT):
        coded_message+=chr(ord(i)-26+SHIFT)

    #Space and punctuation pass-throughs
    else:
        coded_message+=i

#Print encoded message
print(f"The encoded message is: {coded_message}")
