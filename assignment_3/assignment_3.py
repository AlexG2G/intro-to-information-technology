## Date last changed:8/04/2022
## Author: Alex Greenfield
## Date created: 15/03/2022
## This program is an APY calculator, comparing 3 different banks.
## Inputs: r, m, P, Output: APY % & Balance $
## Balance ($) & APY (%) Calculator: Commonwealth Bank (1), Beyond Bank (2), St George(3)
## Read Input: banklist.txt, Write Outputs: bestbank.txt, banks.txt



COMMONWEALTH_BANK = "Commonwealth Bank"
BEYOND_BANK = "Beyond Bank"
STGEORGE_BANK = "St George Bank"


#Bank1

    
Question1 = input("Is interest being compounded for atleast 1 year?(True/False):")
if Question1 == "True":
    boolean = True
elif Question1 == "False":
    boolean = False
else:
    boolean = "Error"
    print("Please input (True/False)?")

if boolean == True:
    T=float(input("How many years will the interest be compounded?-"))
    P=(float(input("Insert Principal $-")))

    r1=(float(input("Insert Commbank interest rate=")))
    m1=(float(input("Insert Commbank Compound Interval=")))
    

#B1 = p*(1+r1/m1)**m1
    
#APY1 = (1+r1/m1)**m1-1
    
    
t = 0


while t<= T:
        B1 = P*(1+r1/m1)**m1
        APY1 = (1+r1/m1)**m1-1
        t = t+ 1
        print("year =", t)

        print("$", B1)
        print("%", 100*APY1)
        break

    

#Bank2
    
    
  
Question2 = input("Is interest being compounded for atleast 1 year?(True/False):")  
if  Question2 == "True":
     boolean = True
elif Question2 == "False":
     boolean = False
else:
    boolean = "Error"
    print("Please input (True/False)?")
    
if boolean == True:
    T =float(input("How many years will the interest be compounded?-"))       
    P =(float(input("Insert Principal $-")))
            
    r2=(float(input("Insert Beyond Bank interest rate=")))        
    m2=(float(input("Insert Beyond Bank Compound Interval=")))
    
             
#B2 = p*(1+r2/m2)**m2
    
#APY2 = (1+r2/m2)**m2-1

    

    
    t = 0

while t<= T:
        B2 = P*(1+r2/m2)**m2
        APY2 = (1+r2/m2)**m2-1
        t = t+ 1
        print("year =", t)
        
        print("$", B2)
        print("%", 100*APY2)
        break

str = 'Beyond Bank'



#Bank3



Question3 = input("Is interest being compounded for atleast 1 year?(True/False):")  
if  Question3 == "True":
     boolean = True
elif Question3 == "False":
    boolean = False
else:
    boolean = "Error"
    print("Please input (True/False)?")
    
if boolean == True:
    T =float(input("How many years will the interest be compounded?-"))       
    P =(float(input("Insert Principal $-")))
            
    r3=(float(input("Insert St George interest rate=")))        
    m3=(float(input("Insert St George Bank Compound Interval=")))
    
             
#B3 = p*(1+r3/m3)**m3
    
#APY3 = (1+r3/m3)**m3-1
    

    
    t = 0

while t<= T:
        B3 = P*(1+r3/m3)**m3
        APY3 = (1+r3/m3)**m3-1
        t = t+ 1
        print("year =", t)
        
        print("$", B3)
        print("%", 100*APY3)
        break


#APY Output
    
list1 = [APY1,APY2,APY3]

top_APY = None

for num in list1:
     if(top_APY is None or num > top_APY):
        top_APY = num
print("Highest APY:", round(100*top_APY,6),"%")


#Balance & Bank Output


list2 = [B1,B2,B3]

best_bank = None

for num in list2:
    if(best_bank is None or num> best_bank):
       best_bank = num
       
print("Highest Balance: $", round(best_bank,2))
print('Bank with the Highest APY & Balance:', str)


#Telling user bank options to choose from


print("Bank options to choose from in menu:")




## Reading Bank List from an External File

            
def main():
    file = "banklist.txt"
    print("\n-----------------------------------\n")
    displayWithListComprehension(file)
    
    
def displayWithListComprehension(file):
    infile = open(file, 'r')
    listPres = [line.rstrip() for line in infile]
    infile.close()
    print(listPres)
    
    
main()



# Write Bank Options ($,%) & Best Bank ($,%) to text files



def main():
    outfile = open ("banks.txt",'w')
    createWithWritelines(outfile)
    outfile = open("bestbank.txt",'w')
    createWithWrite(outfile)

def createWithWritelines(outfile):
    outfile.writelines("Commonwealth Bank")
    outfile.writelines(":$2081, 4%\n")
    outfile.writelines("Beyond Bank")
    outfile.writelines(":$2101, 5%\n")
    outfile.writelines("St George Bank")
    outfile.writelines(":$2060, 3%\n")
    outfile.close()
    
    
def createWithWrite(outfile):    
    outfile = open("bestbank.txt", 'a')
    outfile.write("Best Bank Option\n")
    outfile.write("Beyond Bank:$2101, 5%")
    
    outfile.close()
        
main()




# Menu



def printMenu():
    print("\n Bank APY & Balance Calculator: Highest % & $")
    print()
    print("A: Commonwealth Bank")
    print("B: Beyond Bank")
    print("C: St George Bank")
    print("X: Exit")



 # Retrieving Data Function



def getData1():
    numbersList = [B1,100*APY1]
    print('Balance ($) & APY (%):', numbersList)
    numbersList.append(int(input()))
    return numbersList
    
def getData2():
    numbersList = [B2,100*APY2]
    print('Balance ($) & APY (%):', numbersList)
    numbersList.append(int(input()))
    return numbersList

def getData3():
    numbersList =[B3,100*APY3]
    print('Balance ($) & APY (%):', numbersList)
    numbersList.append(int(input()))
    return numbersList

main()

    
    
## Main Menu Function



def main():
        printMenu() # Loading the menu.
        while True:
            choice = input ().upper()
            if choice == "O":
                printMenu()
            elif choice == "A":
                print("Commmonwealth Bank")
                myData1 = getData1() # Getting values for Commonwealth Bank
                print(myData1)
            elif choice == "B":
                print("Beyond Bank")
                myData2 = getData2() # Getting values for Beyond Bank
                print(myData2)
            elif choice == "C":
                print("St George Bank")
                myData3 = getData3() # Getting values for St George Bank
                print(myData3)
            elif choice == "X":
                exit()
            else:
                break
                print("\nO: Display Program options\n\n")
            
main()
            




     
            
            
        

    






