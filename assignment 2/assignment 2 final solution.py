## Date last changed:21/03/2022
## Author: Alex Greenfield
## Date created: 15/03/2022
## This program is an APY calculator, comparing 3 different banks.
## Input: r, m, P, Output: APY % & Balance $
# APY% Calculator, Commonwealth Bank (1), Beyond Bank (2), St George(3)


#Bank1

    
Question1 = input("Is interest being compounded for 1 year?(True/False):")
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
        print("%", APY1)
        break

#Bank2
  
Question2 = input("Is interest being compounded for 1 year?(True/False):")  
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
        print("%", APY2)
        break

str = 'Beyond Bank'

#Bank3

Question3 = input("Is interest being compounded for 1 year?(True/False):")  
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
        print("%", APY3)
        break

        
list1 = [APY1,APY2,APY3]

top_APY = None

for num in list1:
     if(top_APY is None or num > top_APY):
        top_APY = num
print("Highest APY% in decimal form:", round(top_APY,6),"")

list2 = [B1,B2,B3]

best_bank = None

for num in list2:
    if(best_bank is None or num> best_bank):
       best_bank = num
print("Highest Balance:", round(best_bank,2),"$")

print('Bank with the Highest APY & Balance:', str)



        
        



