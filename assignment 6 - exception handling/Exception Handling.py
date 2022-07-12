### Date last changed:14/05/2022
## Author: Alex Greenfield
## Date created: 13/05/2022

## This program calculates the reciprocal of the integer that is entered.
## It has exception handling that accounts for non integer numbers, division by zero and integers not in range of 1-10.#Define number

## Input: number
## Output: reciprocal

#Define number

number = 0

#While loop asking for input again and again

dict = {"True":(1,2,3,4,5,6,7,8,9,10,),"False":(0,11)}
while True:
    flag = 0  #flag to handle one exception at a time 
    try:  #handling if the number isn't an integer value
        number = int(input("Enter an interger between 1 to 10: "))
    except ValueError:  #print an error message for non interger
        print("You did not enter an integer! \nPlease, try again.\n")
        flag = 1  #updating the flag value after handling error
        #handling if the number is 0
    except ZeroDivisionError: #print an error message  for 0
        print("Oops, You entered Zero! \nPlease,try again.\n")
      
    
    #After handling first error
        
    if flag == 0: 
        try:  
            if number >10:   #for a value other than 1 to 10
                raise ValueError("You did not enter an integer between 1 and 10! \nPlease, try again.\n")
            if number < 1:
                raise ZeroDivisionError("Oops, You entered Zero! \nPlease,try again.\n")
        except ValueError as ve: #handling error and printing a message
            print(ve)
        except ZeroDivisionError as zde:  #if 0 
            print(zde)
        else: #if a valid input
          break  
        
                      
#Calculating the reciprocal

reciprocal = 1 / number

#Printing an output

print("The reciprocal of your number is ", reciprocal)

