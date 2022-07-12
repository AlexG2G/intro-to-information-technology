## Date last changed:25/04/2022
## Author: Alex Greenfield
## Date created: 15/03/2022
## This program is an APY calculator, comparing 3 different banks.
## Inputs: r, m, P, Output: APY % & Balance $
## Balance ($) & APY (%) Calculator: Commonwealth Bank (1), Beyond Bank (2), St George(3)
## Read Input: banklist.txt, Write Outputs: bestbank.txt, banks.txt


#Import the tkinter library


import tkinter as tk
from tkinter import *


#GUI Main


BTN_ENT_WIDTH = 25

def Banks():
    bank = ""
    if chkVarC.get() == 1:
        bank+= "$2081, 4%"
        
    if chkVarB.get() == 1:
        bank+= " $2102, 5.1%"
    
    if chkVarG.get() == 1:
        bank+= "$2061, 3%"
    
   
    txtEnt. set(bank)


window = Tk ()

window.title("Bank APY & Balance List Output")

window.geometry("700x300")

window.configure(bg='navy')


# create a menu bar options
menubar = Menu (window)
Menu = Menu (menubar, tearoff=0)

Menu.add_command(label="Info", command = print('Made by Alex Greenfield, 2022 UC\nThank you for using our program'))


Menu.add_separator() # add a line separating the menu items
Menu.add_command(label="Exit", command=window.destroy)


# create a menu
menubar.add_cascade(label="Details", menu=Menu)
window.config(menu=menubar)

lbl = Label (window, text="Choose Bank Options", font="Calibri 16")
lbl.grid(row=3, column=0, padx=10, sticky=W)


chkVarC = IntVar()#
#chkVarC. set (1) # check the checkbox       
chkC = Checkbutton(window, text = "Commonwealth Bank", variable=chkVarC, font="Calibri 14")
chkC.grid(row=4, column = 0,padx=10, sticky=W)


chkVarB = IntVar()
chkB = Checkbutton(window, text = "Beyond Bank", variable=chkVarB, font="Calibri 14")
chkB.grid(row=5, column=0, padx=10, sticky=W)

chkVarG = IntVar()
chkG = Checkbutton(window, text = "St George Bank", variable=chkVarG, font="Calibri 14")
chkG.grid(row = 6,column = 0,padx=10, sticky=W)


txtEnt= StringVar()
txtEnt. set (" ")
ent= Entry(window, width=BTN_ENT_WIDTH, font= ('Comic Sans M' ,15, "bold"),textvariable=txtEnt)
ent.grid(row=8,column=0, columnspan=1, padx=20,pady=10)

btn= Button(window, text="Display Bank Balance & APY", width=BTN_ENT_WIDTH, command= Banks, font="Calibri 14")
btn.grid(row=9, column = 0, columnspan = 1, padx = 20, pady = 10)

btnQuit= Button(window, text="QUIT",width=BTN_ENT_WIDTH, command=window.destroy, font="Calibri 14")                        
btnQuit.grid(row=9, column = 1, padx=20, pady = 10)


#GUI Calculator Fields


fields = ('Principal','Interest','Compound Interval', 'FINAL_BALANCE','APY')


#APY

def APY(entries):
    try:
        # Interest:
        r = (float(entries['Interest'].get()) / 100) 
        # Principal 
        P = float(entries['Principal'].get())
        # Compound Interval
        n =  float(entries['Compound Interval'].get())
        APY = (1 + r / n) ** n - 1
        entries['APY'].delete(0, tk.END)
        entries['APY'].insert(0, 100*APY )
        print("APY: %", 100*APY)
    except ValueError:  #ValueError if fails
        print("Error, please input an actual number.")
    except ZeroDivisionError: #When divided by 0 it will fail
        print("Invalid. Please do not use zero")


#FINAL_BALANCE
        
def FINAL_BALANCE(entries):
    try:
        # Interest:
        r = (float(entries['Interest'].get()) / 100) 
        # Principal 
        P = float(entries['Principal'].get())
        # Compound Interval
        n =  float(entries['Compound Interval'].get())
        FINAL_BALANCE = P * (1 + r / n) ** n 
        entries['FINAL_BALANCE'].delete(0, tk.END)
        entries['FINAL_BALANCE'].insert(0, FINAL_BALANCE)
        print("Balance: $", FINAL_BALANCE)
    except ValueError: #ValueError if fails
        print("Error, please input an actual number.")
    except ZeroDivisionError: #When divided by 0 it will fail
        print("Invalid. Please do not use zero")
        

#makeform (labels, entries, rows)
        
def makeform(root, fields):
    entries = {}
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
        ent = tk.Entry(row,)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, fill=tk.X,  padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries[field] = ent
    return entries

# GUI Main (bg, buttons, size)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("400x300")
    root.configure(bg='navy')
    root.title("Bank APY & Balance Calculator")
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='APY',command=(lambda e=ents: APY (e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Final Balance',command=(lambda e=ents: FINAL_BALANCE (e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text="QUIT", command=root.destroy)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    

root.mainloop()

            




     
            
            
        

    






