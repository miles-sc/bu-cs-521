# Miles Cameron
# Class: CS 521 - Fall 1
# Date: 9/22/24
# Homework Problem # 3_1
# Description of Problem: This problem requires calculating the amount of
#                         paper needed to cover a box of a certain size, which
#                         is provided by the user

#Introduction
print("Don't waster paper! Let's calculate how much you need.")

#Set up while loop to run until user quits program
run=True
while run:

      #Take input from user
      dim_string=input("Enter the box dimensions, separated with an x, "+\
                        "e.g. 10x20x15: ")
      dim_string+="x"

      #Quit stipulation
      if dim_string=="quitx":
            print("Happy wrapping!")
            run=False

      #Normal operating block
      else:
            #Initialize variables
            dim_float=["","",""]
            dim_counter=0
            dim_temp=""

            #Set up for loop to examine user input and populate variables
            for char in dim_string:

                  #Find break points between dimensions and store data
                  if char=="x":

                        dim_float[dim_counter]=float(dim_temp)
                        dim_temp=""
                        dim_counter+=1

                  else:
                        dim_temp+=char

            #Calculate paper needs using parsed data
            l=dim_float[0]
            w=dim_float[1]
            h=dim_float[2]
            paper_needed=(2*l*w)+(2*l*h)+(2*h*w)+min((l*w),(l*h),(h*w))

            #Print results
            print(f"You will need {str(round(paper_needed))} "+\
                  "square cm of paper.")
