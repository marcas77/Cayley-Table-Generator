"Cayley Table Generator"
"Created by Marcas Anderson"
#Code will find the Cayley Table for U(n), n = what your desired number is,
#Create it, and output it to a new file named "Cayley Table for U(n)"
#Code will also print to console if you'd rather look at console.

import pandas as p

def Zprinter(newZ,mod,xlname):
    biglist = []
    for i in range(0,len(newZ)):
        list3 = []
        for k in range(0,len(newZ)):
                list3.append((newZ[k]+newZ[i]) % mod)
        print(list3)
        biglist.append(list3)
    df = p.DataFrame(biglist,index=newZ,columns=newZ)
    df.to_excel(xlname,freeze_panes=[1,1])
    return


def Uprinter(newU,mod,xlname):
    biglist = []
    for i in range(0,len(newU)):
        list3 = []
        for k in range(0,len(newU)):
                list3.append((newU[k]*newU[i]) % mod)
        print(list3)
        biglist.append(list3)
    "Creates the dataframe we use to hold the biglist"
    df = p.DataFrame(biglist,index=newU,columns=newU)
    "Exports to excel, freezing the first row/column to make viewing larger Cayley Tables easier"
    df.to_excel(xlname,freeze_panes=[1,1])
    return


def Compare(U,mod):
    "Def declares a new list, then compares lists U and mod for any factors from mod (excluding 1)."
    "Function will add all values from U into list2, excluding those factors of mod."
    list2 = U.copy()
    for i in range(1,len(U)):
        for k in range(1,len(mod)):
            if(U[i] % mod[k] == 0):
                print("Found ",U[i]," mod ",mod[k],"= 0. Removing from the list.")
                list2.remove(U[i])
                break
    #print(list2,"endlist")
    return list2


def ModFactors(x):
    "Def declares a list and fills list with factors of input integer."
    list1 = []
    for i in range(1,x+1):
        if(x % i == 0):
            list1.append(i)
    #print(list1,"ModFactors")
    return list1


def declist(U,AddClause):#
    "Def declares a list with numbers 1 through U for the U list."
    list0 = []
    if(AddClause == 1):
        list0.append(0)
    for i in range(1,U):
        list0.append(i)
    #print(list0,"DecList")
    return list0


def Z(n):
    Zlist = declist(n,1)
    xlname = "Cayley Table for Z("+str(n)+").xlsx"
    Zprinter(Zlist,n,xlname)
    
    
def U(n):
    Ulist = declist(n,0)
    modfact = ModFactors(n)
    newU = Compare(Ulist,modfact)
    xlname = "Cayley Table for U("+str(n)+").xlsx"
    Uprinter(newU,n,xlname)
    

def custom(function,n,operation):
    if(operation==0):#Multiplication
        xlname = "Cayley Table under multiplication mod "+str(n)+" for "+str(function)+".xlsx"
        Uprinter(function,n,xlname)
        
    if(operation==1):#Addition
        xlname = "Cayley Table under addition mod "+str(n)+" for "+str(function)+".xlsx"
        Zprinter(function,n,xlname)


def main():
    print("For Zn, use Z(n)")
    print("For Un, use U(n)")
    print("For a specific mod, use custom([],n,operation), where: ") 
    print("[] is the subgroup you are using,")
    print("n is the mod,")
    print("and operation is either adding or multiplying. For addition, use 1. For multiplication, use 0")

    
    