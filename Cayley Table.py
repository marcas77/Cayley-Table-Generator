"Cayley Table Generator"
"Created by Marcas Anderson"
#Code will find the Cayley Table for U(n), n = what your desired number is,
#Create it, and output it to a new file named "Cayley Table for U(n)"
#Code will also print to console if you'd rather look at console.

import pandas as p

def tableprinter(newU,mod,xlname):
    "Def declares a final list which which computes what values should be in the table, then prints them."
    
    "Creates the list we enter into the dataframe at the end to make the xlsx values"
    biglist = []
    for i in range(0,len(newU)):
        list3 = []
        for k in range(0,len(newU)):
            if (k==0):
                # string=str(newU[i])
                # while(len(string)!=largest):
                #     string+=" "
                
                # list3.append(string)
                list3.append(newU[i])
            else:
                x=newU[k]*newU[i]
                if(x > newU[len(newU)-1]):
                    list3.append((newU[k]*newU[i]) % mod)
                else:
                    list3.append((newU[k]*newU[i]))
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
    
    list2 = [1]
    for i in range(1,len(U)):
        for k in range(1,len(mod)):
            if(U[i] % mod[k] != 0):
                list2.append(U[i])
            break
    return list2

def declist(U):
    "Def declares a list with numbers 1 through U for the U list."
    
    list0 = []
    for i in range(1,U+1):
        list0.append(i)
    return list0


def ModFactors(x):
    "Def declares a list and fills list with factors of input integer."
    
    list1 = []
    for i in range(1,x+1):
        if(x % i == 0):
            list1.append(i)
    return list1

def main(U):
    "Creates the file name for the Cayley Table"
    
    xlname = "Cayley Table for U("+str(U)+").xlsx"
    "Runs the important defs"
    Ulist = declist(U)
    modfact = ModFactors(U)
    newU = Compare(Ulist,modfact)
    tableprinter(newU,U,xlname)