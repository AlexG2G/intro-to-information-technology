## Date last changed:15/05/2022
## Author: Alex Greenfield
## Date created: 13/05/2022

## This program calculates the reciprocal of the valid integer that is entered.
## It has exception handling that accounts for non integer numbers, division by zero and integers not in range of 1-10.

## Input: number
## Output: reciprocal


#Dictionary of valid integers
dict = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}

#While loop asking for input again and again
while True: 
    try:  #requests user to input a number between 1 and 10
        number = dict[input("Enter an integer between 1 and 10: ")]
        #calculating the reciprocal
        reciprocal = 1 / number
        #printing valid input
        print("That integer is valid.")
        #printing an output
        print("The reciprocal of your number is ", reciprocal)
        break
        #exception handling 
    except KeyError:
        print("That integer is not within the range, is 0 or is not an integer. \nPlease, try again.\n")
        
         
         
         




