import Tkinter
import ttk
import Tkinter as tk
from Tkinter import *
from Tkinter import *
#from Tkinter import ttk
from Tkinter import Menu
import tkMessageBox
import unittest

root = Tk()
root.title("Tax Calculator")
root.geometry("1000x600")




tabControl = ttk.Notebook(root) 
tabControl.pack(expand=1, fill="both")  

incomenumber = DoubleVar()
MPFnum = DoubleVar()
DEDUCTIONS= DoubleVar()
totallowancenum = DoubleVar()
netincomenum = DoubleVar()
Taxsolopay = DoubleVar()

incomenumber.set('')
MPFnum.set(0)
Taxsolopay.set('')
DEDUCTIONS.set('')
totallowancenum.set('')
netincomenum.set('')
MPFnum.set('')

Tax = ttk.Frame(tabControl)  
tabControl.add(Tax, text='Tax')
monty = ttk.LabelFrame(Tax, text='Tax')

##auto
def Cal1people(int_income,int_mpf):
    
    if int_income <=132000: ##No tax payable##
            tax = 0
            return tax
    elif int_income < 2040050:
        net_chargeable_income= int(int_income-int_mpf-132000)
        
        Check = net_chargeable_income
       
        if net_chargeable_income > 0:
            if Check <= 49999:               
                tax = int(net_chargeable_income*0.02)
                
                return tax
            elif Check >= 50000 and Check <=99999:
                on9=net_chargeable_income-50000
                tax=int((on9*0.06)+1000)
                
                return tax
            elif Check >= 100000 and Check <=149999:
                on9j=net_chargeable_income-100000
                tax= int((on9j*0.1)+4000)
                
                return tax
            elif Check >= 150000 and Check <=199999:
                on9pui=net_chargeable_income-150000
                tax=int((on9pui*0.14)+9000)
                
                return tax
            elif Check >= 200000:
                puipui=net_chargeable_income-200000
                tax=int((puipui*0.17)+16000)
                
                return tax
           
    else:
        aaronB=int_income-int_mpf
        tax=int(aaronB*0.15)
        
        return tax
        
def Cal2peopleSelfnSpouse(SelfIncome,SpouseIncome,SelfMPF,SpouseMPF):
    global sesp

    
    #Self#
    if SelfIncome <2040050:
        Selfcome = int(SelfIncome-SelfMPF-132000)
        if Selfcome>0:
            if Selfcome >=200000:
                se = int((Selfcome-200000)*0.17)+16000
            elif Selfcome >=150000 and Selfcome<=199999:
                se = int((Selfcome-150000)*0.14)+9000
            elif Selfcome >=100000 and Selfcome<=149999:
                se = int((Selfcome-100000)*0.1)+4000
            elif Selfcome >=50000 and Selfcome<=99999:
                se = int((Selfcome-50000)*0.06)+1000
            else:
                se = int(Selfcome)*0.02
        else:
            print 'hi'
    else:
        Selfcome2 = int(SelfIncome-SelfMPF)
        se = int(Selfcome2*0.15)



    
     #Spouse#   
    if SpouseIncome <2040050:
        Spousecome = int(SpouseIncome-SpouseMPF-132000)
        if Spousecome>0:
            if Spousecome >=200000:
                sp = int((Spousecome-200000)*0.17)+16000

            elif Spousecome >=150000 and Spousecome<=199999:
                sp = int((Spousecome-150000)*0.14)+9000

            elif Spousecome >=100000 and Spousecome<=149999:
                sp = int((Spousecome-100000)*0.1)+4000
  
            elif Spousecome >=50000 and Spousecome<=99999:
                sp = int((Spousecome-50000)*0.06)+1000

            else:
                sp = int(Spousecome)*0.02
  
        else:
            print 'hi'
    else:
        Spousecome2 = int(SpouseIncome-SpouseMPF)
        sp = int(Spousecome2*0.15)
        
        

    sesp = se+sp
    return sesp

def Cal2peopletotal(SelfIncome,SpouseIncome, SelfMPF,SpouseMPF):
    global count
    allcome = SelfIncome+SpouseIncome
    MPFtotal= SelfMPF+SpouseMPF
    if allcome <=264000:    ##No tax payable##
        count = int(0)
        return count
    elif allcome < 3180024:
        total = int(allcome-MPFtotal-264000)
        
        if total>0:
            if total >=200000:
                count = ((total-200000)*0.17)+16000
                return count

            elif total >=150000 and total<=199999:
                count = ((total-150000)*0.14)+9000
                return count
   
            elif total >=100000 and total<=149999:
                count = ((total-100000)*0.1)+4000
                return count
                
            elif total >=50000 and total<=99999:
                count = ((total-50000)*0.06)+1000
                return count
            else:
                count = (total)*0.02
                return count
    else:
        total = int(allcome-MPFtotal)
        count=int(total*0.15)
        return count



def Checknum(sesp,count):
    if sesp <= count:
        return 'Suggest using Separate Taxation which are lower tax'
    elif sesp >= count:
        return 'Suggest using Joint Assessment which are lower tax'
    else:
        return 'No suggestion, Same Tax payable'
        
        


def Cal():  ##1 people##
    if incomenumber.get():
        totallowance.insert(INSERT,'132000')  
        solo = incomenumber.get()
        solomonth = solo/12
        if solomonth < 7099:
            MPF2 = 0
        elif solomonth>=7100 and solomonth<30000:
            MPF2 = solo*0.05
        else:
            MPF2 = 18000
        MPF.insert(INSERT,int(MPF2))

        
        if incomenumber.get() <=132000: ##No tax payable##
            deduct.insert(INSERT,0)
            netincome.insert(INSERT,0)
            Taxpay.insert(INSERT,0)
                
        
        elif incomenumber.get() >=2040050:
            deduct.insert(INSERT,MPF2)
            Calnetincome = incomenumber.get() - 18000
            Calnetincome2= Calnetincome-132000
            netincome.insert(INSERT,Calnetincome2)
            counttax = int(Calnetincome*0.15)
            Taxpay.insert(INSERT,counttax)
            tkMessageBox.showinfo("Annual Income Levels","Your income approach the Standard Rate Zone. It will using Standard Rate")
       
        else:
            if MPF2 == 0:
                da2= incomenumber.get() - 132000
                deduct.insert(INSERT,int(MPF2))
                netincome.insert(INSERT,int(da2))
                if da2 == 0 or da2 <= 0:
                    Taxpay.insert(INSERT,0)
                elif da2 >= 1 and da2 <= 49999 :
                    ba = netincomenum.get()
                    ba2 = ba*0.02
                    Taxp1 = ba2
                    Taxpay.insert(INSERT,int(Taxp1))
                elif da2>= 50000 and da2 <= 99999 :
                    ba = netincomenum.get() - 50000
                    ba2 = ba*0.06
                    Taxp1 = 1000+ba2
                    Taxpay.insert(INSERT,int(Taxp1))   
                elif da2 >= 100000 and da2 <= 149999 :
                    ba = netincomenum.get() - 100000
                    ba2 = ba*0.10
                    Taxp1 = 4000+ba2
                    Taxpay.insert(INSERT,int(Taxp1))   
                elif da2 >= 150000 and da2 <= 199999 :
                    ba = da2 - 150000
                    ba2 = ba*0.14
                    Taxp1 = 9000+ba2
                    Taxpay.insert(INSERT,int(Taxp1))
    
                elif da2 >= 200000:
                    print '1299'
                    ba = netincomenum.get() - 200000
                    ba2 = ba*0.17
                    Taxp1 = 16000+ba2
                    Taxpay.insert(INSERT,int(Taxp1))

                
                
            elif MPF2 >=1 and MPF2 <= 18000:
                da= incomenumber.get() - 132000 - MPF2
                mc = MPFnum.get()
                deduct.insert(INSERT,int(mc))
                if da <=0:
                    netincome.insert(INSERT,0)
                    axpay.insert(INSERT,0)
                else:
                    netincome.insert(INSERT,int(da))
                    if da >= 200000:
                        ba = netincomenum.get() - 200000
                        ba2 = ba*0.17
                        Taxp1 = 16000+ba2
                        Taxpay.insert(INSERT,int(Taxp1))
                    elif da >= 150000 and da <= 199999 :
                        ba = netincomenum.get() - 150000
                        ba2 = ba*0.14
                        Taxp1 = 9000+ba2
                        Taxpay.insert(INSERT,int(Taxp1))
    
                    elif da >= 100000 and da <= 149999 :
                        ba = netincomenum.get() - 100000
                        ba2 = ba*0.10
                        Taxp1 = 4000+ba2
                        Taxpay.insert(INSERT,int(Taxp1))

                    elif da >= 50000 and da <= 99999 :
                        ba = netincomenum.get() - 50000
                        ba2 = ba*0.06
                        Taxp1 = 1000+ba2
                        Taxpay.insert(INSERT,int(Taxp1))
                    elif da <= 49999:
                        ba = netincomenum.get()
                        ba2 = ba*0.02
                        Taxp1 = ba2
                        Taxpay.insert(INSERT,int(Taxp1))
                    else:
                        print 'a'
                
                
                
            elif MPF2 >=18001:
                tkMessageBox.showinfo("MPF ","The deductible Mandatory Contributions to Recognized Retirement Schemes cannot exceed 18,000.")
                MPFnum.set(18000)
                deduct.insert(INSERT,18000)
                fa = incomenumber.get() - 132000 - MPF2
                if fa <=0:
                    netincome.insert(INSERT,0)
                else:
                    netincome.insert(INSERT,int(fa))
                    if fa >= 200000:
                        ba = netincomenum.get() - 200000
                        ba2 = ba*0.17
                        Taxp1 = 16000+ba2
                        Taxpay.insert(INSERT,int(Taxp1))
                    elif fa >= 150000 and fa <= 199999 :
                        ba = netincomenum.get() - 150000
                        ba2 = ba*0.14
                        Taxp1 = 9000+ba2
                        Taxpay.insert(INSERT,int(Taxp1))
    
                    elif fa >= 100000 and fa <= 149999 :
                        ba = netincomenum.get() - 100000
                        ba2 = ba*0.10
                        Taxp1 = 4000+ba2
                        Taxpay.insert(INSERT,int(Taxp1))

                    elif fa >= 50000 and fa <= 99999 :
                        ba = netincomenum.get() - 50000
                        ba2 = ba*0.06
                        Taxp1 = 1000+ba2
                        Taxpay.insert(INSERT,int(Taxp1))
                    elif fa <= 49999:
                        ba = netincomenum.get()
                        ba2 = ba*0.02
                        Taxp1 = ba2
                        Taxpay.insert(INSERT,int(Taxp1))
                    else:
                        print 'a'
           
            else:
                print 'IFworng2'

    else:
            print 'IFwrong'



def Cal2(): ##2 people total##
    allcome = SelfIncome.get()+SpouseIncome.get()
    Tolincome.insert(INSERT, int(allcome))
    totalal2.insert(INSERT,'132000')    
    totalal3.insert(INSERT,'132000')    
    totalal4.insert(INSERT,'264000')
    Self = SelfIncome.get()
    Spouse = SpouseIncome.get()
    incomea = int(SelfIncome.get())
    monthincome = incomea/12
    incomeb = int(SpouseIncome.get())
    monthincomeb = incomeb/12
    if monthincome < 7099:
        SelfMPF = 0
    elif monthincome>=7100 and monthincome<30000:
        SelfMPF = incomea*0.05
    else:
        SelfMPF = 18000
    if monthincomeb < 7099:
        SpouseMPF = 0
    elif monthincomeb>=7100 and monthincomeb<30000:
        SpouseMPF = incomeb*0.05
    else:
        SpouseMPF = 18000

    
    MPFtotal = SelfMPF+SpouseMPF
    MPFp4.insert(INSERT,MPFtotal)
    deduct2.insert(INSERT,SelfMPF)
    deduct3.insert(INSERT,SpouseMPF)
    deductcount = MPFtotal
    deduct4.insert(INSERT,deductcount)
    
    if allcome <=264000:    ##No tax payable##
        total=int(0)
        netincome4.insert(INSERT, total)
        Taxpayboth3.insert(INSERT, total)
        Totaltax2.insert(INSERT, total)
    elif allcome < 3180024:
        total = int(allcome-MPFtotal-264000)
        netincome4.insert(INSERT, total)
        
        if total>0:
            if total >=200000:
                t1 = int((total-200000)*0.17)
                t2 = t1 +16000
                Taxpayboth3.insert(INSERT, t2)
                Totaltax2.insert(INSERT, t2)
            elif total >=150000 and total<=199999:
                t1 = int((total-150000)*0.14)
                t2 = t1 +9000
                Taxpayboth3.insert(INSERT, t2)
                Totaltax2.insert(INSERT, t2)
            elif total >=100000 and total<=149999:
                t1 = int((total-100000)*0.1)
                t2 = t1 +4000
                Taxpayboth3.insert(INSERT, t2)   
                Totaltax2.insert(INSERT, t2)
            elif total >=50000 and total<=99999:
                t1 = int((total-50000)*0.06)
                t2 = t1 +1000
                Taxpayboth3.insert(INSERT, t2)   
                Totaltax2.insert(INSERT, t2)
            else:
                t1 = int((total)*0.02)
                Taxpayboth3.insert(INSERT, t1)   
                Totaltax2.insert(INSERT, t1)
    else:
        total = int(allcome-MPFtotal)
        total2 = int(allcome-MPFtotal-264000)
        netincome4.insert(INSERT, total2)
        count=int(total*0.15)
        Taxpayboth3.insert(INSERT, count)   
        Totaltax2.insert(INSERT, count)

    
def Cal2SelfnSpouse(): ##2people##
    Self = SelfIncome.get()
    Spouse = SpouseIncome.get()
    incomea = int(SelfIncome.get())
    monthincome = incomea/12
    incomeb = int(SpouseIncome.get())
    monthincomeb = incomeb/12
    
    if monthincome < 7099:
        SelfMPF = 0
        MPFp2.insert(INSERT,SelfMPF)
    elif monthincome>=7100 and monthincome<30000:
        SelfMPF = incomea*0.05
        MPFp2.insert(INSERT,SelfMPF)
    else:
        SelfMPF = 18000
        MPFp2.insert(INSERT,SelfMPF)
        
        
    
    if monthincomeb < 7099:
        SpouseMPF = 0
        MPFp3.insert(INSERT,SpouseMPF)
    elif monthincomeb>=7100 and monthincomeb<30000:
        SpouseMPF = incomeb*0.05
        MPFp3.insert(INSERT,SpouseMPF)
        
    else:
        SpouseMPF = 18000
        MPFp3.insert(INSERT,SpouseMPF)
    
    
    
    
    
    #Self#
    
    
    
    if Self>=0 and Self<=139000:
        Selfcome = 0
        netincome2.insert(INSERT, Selfcome)
        t2 = 0
        Taxpayboth.insert(INSERT, int(t2))
        if Selfcome>0:
            if Selfcome >=200000:
                t2 = ((Selfcome-200000)*0.17)+16000
                print t2
                Taxpayboth.insert(INSERT, int(t2))
            elif Selfcome >=150000 and Selfcome<=199999:
                t2 = ((Selfcome-150000)*0.14)+9000
                Taxpayboth.insert(INSERT, int(t2))
            elif Selfcome >=100000 and Selfcome<=149999:
                t2 = ((Selfcome-100000)*0.1)+4000
                Taxpayboth.insert(INSERT, int(t2))   
            elif Selfcome >=50000 and Selfcome<=99999:
                t2 = ((Selfcome-50000)*0.06)+1000
                Taxpayboth.insert(INSERT, int(t2))   
            else:
                t2 = (Selfcome)*0.02
                Taxpayboth.insert(INSERT, int(t2))  
        else:
            print 'hi'
    
    elif Self <2040050:
        Selfcome = int(Self-SelfMPF-132000)
        netincome2.insert(INSERT, Selfcome)
        if Selfcome>0:
            if Selfcome >=200000:
                t2 = ((Selfcome-200000)*0.17)+16000
                print t2
                Taxpayboth.insert(INSERT, int(t2))
            elif Selfcome >=150000 and Selfcome<=199999:
                t2 = ((Selfcome-150000)*0.14)+9000
                Taxpayboth.insert(INSERT, int(t2))
            elif Selfcome >=100000 and Selfcome<=149999:
                t2 = ((Selfcome-100000)*0.1)+4000
                Taxpayboth.insert(INSERT, int(t2))   
            elif Selfcome >=50000 and Selfcome<=99999:
                t2 = ((Selfcome-50000)*0.06)+1000
                Taxpayboth.insert(INSERT, int(t2))   
            else:
                t2 = (Selfcome)*0.02
                Taxpayboth.insert(INSERT, int(t2))  
        else:
            print 'hi'
    
 
    else:
        Selfcome = int(Self-SelfMPF)
        netcome = int(Self-SelfMPF-132000)
        netincome2.insert(INSERT, int(netcome))
        t2 = int(Selfcome*0.15)
        Taxpayboth.insert(INSERT, int(t2)) 


    
     #Spouse#   
    if Spouse>=0 and Spouse<=139000:
        Spousecome = 0
        netincome3.insert(INSERT, Spousecome)
        t1 = 0
        Taxpayboth2.insert(INSERT, int(t1))
 
    elif Spouse <2040050:
        Spousecome = int(Spouse-SpouseMPF-132000)
        netincome3.insert(INSERT, Spousecome)
        if Spousecome>0:
            if Spousecome >=200000:
                t1 = ((Spousecome-200000)*0.17)+16000
                print t1
                Taxpayboth2.insert(INSERT, int(t1))
                
            elif Spousecome >=150000 and Spousecome<=199999:
                t1 = ((Spousecome-150000)*0.14)+9000
                Taxpayboth2.insert(INSERT, int(t1))
            elif Spousecome >=100000 and Spousecome<=149999:
                t1 = ((Spousecome-100000)*0.1)+4000
                Taxpayboth2.insert(INSERT, int(t1)) 
            elif Spousecome >=50000 and Spousecome<=99999:
                t1 = ((Spousecome-50000)*0.06)+1000
                Taxpayboth2.insert(INSERT, int(t1))   
            else:
                t1 = (Spousecome)*0.02
                Taxpayboth2.insert(INSERT, int(t1))  
        else:
            print 'hi'
    else:
        Spousecome = int(Spouse-SpouseMPF)
        t1 = int(Spousecome*0.15)
        netcome2 = int(Self-SelfMPF-132000)
        netincome3.insert(INSERT, int(netcome2))
        Taxpayboth2.insert(INSERT, int(t1))  
        
    a = Taxpayboth2.get()
    b = Taxpayboth.get()
    
    check = t1+t2
    Totaltax.insert(INSERT, int(check))


def Run2def():
        try:
            Self = SelfIncome.get()
            Spouse = SpouseIncome.get()
            if Self>=0 and Spouse>=0:
                print "hi"
            else:
                tkMessageBox.showinfo("Error ","You need to input the vaild income")
                return
        except ValueError:
            tkMessageBox.showinfo("Error ","You need to input the vaild income")
        else:
            Cal2()
            Cal2SelfnSpouse()
            Check()
          #  print 'IFwrong'

    



def Check():
    a =totaltax.get()
    b =totaltax2.get()
    if a < b:
        print 'Suggest using Separate Taxation which are lower tax'
        tkMessageBox.showinfo("Suggestion ","Suggest using Separate Taxation which are lower tax")
        Ztest.set('Suggest using Separate Taxation')

    elif b < a:
        print 'Suggest using Joint Assessment which are lower tax'
        tkMessageBox.showinfo("Suggestion ","Suggest using Joint Assessment which are lower tax")
        Ztest.set('Suggest using Joint Assessment')

    else:
        print 'No suggestion, Same Tax payable'
        tkMessageBox.showinfo("No suggestion ","No suggestion, Same Tax payable")
        Ztest.set('No suggestion, Same Tax payable')

def Reset():
    incomenumber.set('')
    MPFnum.set('')
    Taxsolopay.set('')
    DEDUCTIONS.set('')
    totallowancenum.set('')
    netincomenum.set('')

def Reset2():
    MPFnum2.set('')
    MPFnum3.set('')
    MPFnum4.set('')
    SelfIncome.set('')
    SpouseIncome.set('')
    Allincome.set('')
    DEDUCTIONS2.set('')
    DEDUCTIONS3.set('')
    DEDUCTIONS4.set('')
    totallow2.set('')
    totallow3.set('')
    totallow4.set('')
    netin2.set('')
    netin3.set('')
    netin4.set('')
    Taxpay2p.set('')
    Taxpay2p2.set('')
    Taxpay2p3.set('')
    totaltax.set('')
    totaltax2.set('')
    Ztest.set('')



monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(monty, text="Income:").grid(column=0, row=0, sticky='W')
Income = ttk.Entry(monty, width=12, textvariable=incomenumber)
Income.grid(column=1, row=0, sticky='W')

ttk.Label(monty, text="MPF:").grid(column=0, row=1, sticky='W')
MPF= ttk.Entry(monty, width=12, textvariable=MPFnum)
MPF.grid(column=1, row=1, sticky='W')

action = ttk.Button(monty,text="Calculate",width=10, command=Cal)
action.grid(column=2,row=0)

action = ttk.Button(monty,text="Clear",width=10, command=Reset)
action.grid(column=3,row=0)


ttk.Label(monty, text="-----------------------------------------------").grid(column=0, row=2,columnspan=2)



ttk.Label(monty, text="DEDUCTIONS:").grid(column=0, row=3, sticky='W')
deduct= ttk.Entry(monty, width=12, textvariable=DEDUCTIONS)
deduct.grid(column=1, row=3, sticky='W')

ttk.Label(monty, text="TOTAL ALLOWANCES").grid(column=0, row=4, sticky='W')
totallowance= ttk.Entry(monty, width=12, textvariable=totallowancenum)
totallowance.grid(column=1, row=4, sticky='W')


ttk.Label(monty, text="NET CHARGEABLE INCOME").grid(column=0, row=5, sticky='W')
netincome= ttk.Entry(monty, width=12, textvariable=netincomenum)
netincome.grid(column=1, row=5, sticky='W')



ttk.Label(monty, text="TAX PAYABLE BY YOU:").grid(column=0, row=6, sticky='W')
Taxpay = ttk.Entry(monty, width=12, textvariable=Taxsolopay)
Taxpay.grid(column=1, row=6, sticky='W')


ttk.Label(monty, text="-----------------------------------------------").grid(column=0, row=7,columnspan=2)

ttk.Label(monty, text="You need to pay:").grid(column=0, row=8, sticky='W')
Taxpay2 = ttk.Entry(monty, width=12, textvariable=Taxsolopay)
Taxpay2.grid(column=1, row=8, sticky='W')




#Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2##Page2#

Tax2 = ttk.Frame(tabControl)  
tabControl.add(Tax2 , text='HusbandWifeTax')
monty = ttk.LabelFrame(Tax2, text='Separate Taxation and Joint Assessment ')
monty.grid(column=0, row=0, padx=8, pady=4)

SelfIncome = tk.DoubleVar()
SpouseIncome = tk.DoubleVar()
Allincome= tk.DoubleVar()
MPFnum2 = tk.DoubleVar()
MPFnum3 = tk.DoubleVar()
MPFnum4 = tk.DoubleVar()

DEDUCTIONS2 = tk.DoubleVar()
DEDUCTIONS3 = tk.DoubleVar()
DEDUCTIONS4 = tk.DoubleVar()
totallow2 = tk.DoubleVar()
totallow3 = tk.DoubleVar()
totallow4 = tk.DoubleVar()
netin2 = tk.DoubleVar()
netin3 = tk.DoubleVar()
netin4 = tk.DoubleVar()
Taxpay2p= tk.DoubleVar()
Taxpay2p2= tk.DoubleVar()
Taxpay2p3= tk.DoubleVar()
totaltax= tk.DoubleVar()
totaltax2= tk.DoubleVar()

ttk.Label(monty, text="Separate Taxation:").grid(column=0, row=0, sticky='W')
ttk.Label(monty, text="Joint Assessment:").grid(column=4, row=0, sticky='W')

SelfIncome.set('')
SpouseIncome.set('')
Allincome.set('')
DEDUCTIONS2.set('')
DEDUCTIONS3.set('')
DEDUCTIONS4.set('')
totallow2.set('')
totallow3.set('')
totallow4.set('')
netin2.set('')
netin3.set('')
netin4.set('')
Taxpay2p.set('')
Taxpay2p2.set('')
Taxpay2p3.set('')
totaltax.set('')
totaltax2.set('')
MPFnum4.set('')
MPFnum2.set('')
MPFnum3.set('')





























ttk.Label(monty, text="Self Income:").grid(column=0, row=1, sticky='W')
self= ttk.Entry(monty, width=12, textvariable=SelfIncome)
self.grid(column=1, row=1, sticky='W')


ttk.Label(monty, text="Spouse Income:").grid(column=2, row=1, sticky='W')
spouse= ttk.Entry(monty, width=12, textvariable=SpouseIncome)
spouse.grid(column=3, row=1, sticky='W')

ttk.Label(monty, text="Total Income:").grid(column=4, row=1 ,sticky='W')
Tolincome= ttk.Entry(monty, width=12, textvariable=Allincome)
Tolincome.grid(column=5, row=1, sticky='W')

ttk.Label(monty, text="MPF:").grid(column=0, row=2, sticky='W')
MPFp2= ttk.Entry(monty, width=12, textvariable=MPFnum2)
MPFp2.grid(column=1, row=2, sticky='W')


MPFp3= ttk.Entry(monty, width=12, textvariable=MPFnum3)
MPFp3.grid(column=3, row=2, sticky='W')

ttk.Label(monty, text="Total MPF:").grid(column=4, row=2, sticky='W')
MPFp4= ttk.Entry(monty, width=12, textvariable=MPFnum4)
MPFp4.grid(column=5, row=2, sticky='W')


action = ttk.Button(monty,text="Calculate",width=10, command=Run2def)
action.grid(column=6,row=1)

action = ttk.Button(monty,text="Clear",width=10, command=Reset2)
action.grid(column=7,row=1)

ttk.Label(monty, text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").grid(column=0, row=3,columnspan=8)

ttk.Label(monty, text="DEDUCTIONS:").grid(column=0, row=4, sticky='W')

deduct2= ttk.Entry(monty, width=12, textvariable=DEDUCTIONS2)
deduct2.grid(column=1, row=4, sticky='W')

deduct3= ttk.Entry(monty, width=12, textvariable=DEDUCTIONS3)
deduct3.grid(column=3, row=4, sticky='W')


deduct4= ttk.Entry(monty, width=12, textvariable=DEDUCTIONS4)
deduct4.grid(column=5, row=4, sticky='W')


ttk.Label(monty, text="TOTAL ALLOWANCES").grid(column=0, row=5, sticky='W')

totalal2= ttk.Entry(monty, width=12, textvariable=totallow2)
totalal2.grid(column=1, row=5, sticky='W')

totalal3= ttk.Entry(monty, width=12, textvariable=totallow3)
totalal3.grid(column=3, row=5, sticky='W')

totalal4= ttk.Entry(monty, width=12, textvariable=totallow4)
totalal4.grid(column=5, row=5, sticky='W')

ttk.Label(monty, text="NET CHARGEABLE INCOME").grid(column=0, row=6, sticky='W')

netincome2= ttk.Entry(monty, width=12, textvariable=netin2)
netincome2.grid(column=1, row=6, sticky='W')

netincome3= ttk.Entry(monty, width=12, textvariable=netin3)
netincome3.grid(column=3, row=6, sticky='W')


netincome4= ttk.Entry(monty, width=12, textvariable=netin4)
netincome4.grid(column=5, row=6, sticky='W')

ttk.Label(monty, text="TAX PAYABLE:").grid(column=0, row=7, sticky='W')

Taxpayboth = ttk.Entry(monty, width=12, textvariable=Taxpay2p)
Taxpayboth.grid(column=1, row=7, sticky='W')

Taxpayboth2 = ttk.Entry(monty, width=12, textvariable=Taxpay2p2)
Taxpayboth2.grid(column=3, row=7, sticky='W')

Taxpayboth3 = ttk.Entry(monty, width=12, textvariable=Taxpay2p3)
Taxpayboth3.grid(column=5, row=7, sticky='W')

ttk.Label(monty, text="-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------").grid(column=0, row=8,columnspan=8)

ttk.Label(monty, text="Total Tax:").grid(column=0, row=9, sticky='W')


Totaltax = ttk.Entry(monty, width=38, textvariable=totaltax)
Totaltax.grid(column=1, row=9, sticky='W', columnspan=4)

Totaltax2 = ttk.Entry(monty, width=12, textvariable=totaltax2)
Totaltax2.grid(column=5, row=9, sticky='W')

ttk.Label(monty, text="Suggest:").grid(column=0, row=10, sticky='W')
Ztest = StringVar()
Z = ttk.Entry(monty, width=65 ,textvariable=Ztest)
Z.grid(column=1, row=10, columnspan = 10,sticky='W')




root.mainloop()
