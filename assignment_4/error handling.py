## Date last changed:25/04/2022
## Author: Alex Greenfield
## Date created: 15/03/2022
## This program is an APY calculator, comparing 3 different banks.
## Inputs: r, m, P, Output: APY % & Balance $
## Balance ($) & APY (%) Calculator: Commonwealth Bank (1), Beyond Bank (2), St George(3)
## Read Input: banklist.txt, Write Outputs: bestbank.txt, banks.txt

##Error Handling

#Time Input & Decision

    
try:
    T = int(input("How many years are you compounding interest?(must be ≥ 1):"))
    T0 = T * 1 / T #Do not use zero (This is here so 0 shows invalid)
except ValueError:    #ValueError if fails                            
    print("\nYou did not respond with an integer value. ")
except ZeroDivisionError: #When divided by 0 it will fail
    print("Invalid. Please do not use zero")
    

#Principal Input
    

try:
    P = int(input("\nEnter Principal Here: $"))
    P0 = P * 1 / P #Do not use zero (This is here so 0 shows invalid)
except ValueError: #ValueError if fails                            
    print("\nYou did not respond with an integer value. ")
except ZeroDivisionError: #When divided by 0 it will fail
    print("Invalid. Please do not use zero")



#Bank 1
    

try:
    r1 = float(input('\nEnter the interest in decimal form (%): '))
    m1 = int(input('Enter the Compound Interval:'))
    B1 = P *( 1 +  r1 / m1 )** m1
    APY1 = ( 1 +  r1 /  m1 )**  m1 - 1
    print('\nBalance, Bank 1: $', B1)
    print('APY, Bank 1: ', 100*APY1,'%')
except ValueError: #ValueError if fails  
    print("Error, please input an actual number.")
except ZeroDivisionError: #When divided by 0 it will fail
    print("Invalid. Please do not use zero")

t = 0


while t<= T:
        B1 = P*(1+r1/m1)**m1
        APY1 = (1+r1/m1)**m1-1
        t = t+ 1
        print("Years Compounded =", t)
        break
    

#Bank 2
    

try:
    r2 = float(input('\nEnter the interest in decimal form (%): '))
    m2 = int(input('Enter the Compound Interval:'))
    B2 = P *( 1 + r2 / m2 )** m2
    APY2 = ( 1 + r2 / m2 )** m2 - 1
    print('\nBalance, Bank 2: $', B2)
    print('APY, Bank 2: ', 100*APY2,'%')
except ValueError: #ValueError if fails  
    print("Error, please input an actual number.")
except ZeroDivisionError: #When divided by 0 it will fail
    print("Invalid. Please do not use zero")

t = 0

while t<= T:
        B2 = P *(1+r2/m2)**m2
        APY2 = (1+r2/m2)**m2-1
        t = t+ 1
        print("Years Compounded =", t)
        break

str = 'Beyond Bank'


    
#Bank 3


try:
    r3 = float(input('\nEnter the interest in decimal form (%): '))
    m3 = int(input('Enter the Compound Interval:'))
    B3 = P *( 1 + r3 /  m3 )** m3
    APY3 = ( 1 + r3 / m3 )** m3 - 1
    print('\nBalance, Bank 3: $', B3)
    print('APY, Bank 3: ', 100*APY3,'%')
except ValueError: #ValueError if fails  
    print("Error, please input an actual number.")
except ZeroDivisionError: #When divided by 0 it will fail
    print("Invalid. Please do not use zero")

t = 0

while t<= T:
        B3 = P*(1+r3/m3)**m3
        APY3 = (1+r3/m3)**m3-1
        t = t+ 1
        print("Years Compounded =", t)
        break


#APY Output
    
    
list1 = [APY1,APY2,APY3]

top_APY = None

for num in list1:
     if(top_APY is None or num > top_APY):
        top_APY = num
print('\nBank with the Highest APY & Balance:', str)
print("\nHighest APY:", round(100*top_APY,6),"%")


#Balance & Bank Output


list2 = [B1,B2,B3]

best_bank = None

for num in list2:
    if(best_bank is None or num> best_bank):
       best_bank = num
       
print("Highest Balance: $", round(best_bank,2))



#Write Bank Options ($,%) & Best Bank ($,%) to text files


def main():
    outfile = open ("banks.txt",'w')
    createWithWritelines(outfile)
    outfile = open("bestbank.txt",'w')
    createWithWrite(outfile)
    outfile.close()

def createWithWritelines(outfile):
    outfile.writelines("Commonwealth Bank")
    outfile.writelines(":$2081, 4%\n")
    outfile.writelines("Beyond Bank")
    outfile.writelines(":$2101, 5%\n")
    outfile.writelines("St George Bank")
    outfile.writelines(":$2060, 3%\n")
    outfile.close()

try:
    infile = open ("banks.txt","r")   
    banks = int(infile.readline())   
    print("All Banks:", banks)
except FileNotFoundError: # FileNotFound if fails
    print("File banks.txt not found.")
except ValueError: #ValueError if fails 
    print("\nbanks.txt contains all bank options, and their Balance and APY.")
    infile.close()
else:
    infile.close()
    
    
def createWithWrite(outfile):    
    outfile = open("bestbank.txt", 'a')
    outfile.write("Best Bank Option\n")
    outfile.write("Beyond Bank:$2101, 5%")
    
    outfile.close()
    
try:
    infile = open ("bestbank.txt","r")   
    bestbank = int(infile.readline())   
    print("Best Bank:", bestbank)
except FileNotFoundError: # FileNotFound if fails
    print("File bestbank.txt not found.")
except ValueError: #ValueError if fails 
    print("\nbestbank.txt contains the best bank option.\n")
    infile.close()
else:
    infile.close()


main()
    
    
#Reading Bank / Bank List from an External File

            
def main():
    file = "banklist.txt"
    displayWithListComprehension(file)
    
    
def displayWithListComprehension(file):      
    try:                               
        infile = open(file, 'r') 
        listPres = [line.rstrip() for line in infile]
        infile.close()
        print("banklist.txt found, displayed below:\n")
        print(listPres,"\n")
    except FileNotFoundError: # FileNotFound if fails      
        print("File banklist.txt not found.")
    finally:  
        print("Thank you for using our program\n.")
        infile.close()

main()
