import pandas as pd
import numpy as np
import math as mt
import string
import openpyxl

rows = []
file = []
fileExist = False
fileName = None
column = None
ris = None
columnType = int

def CheckNullRow(row):
    totalLength = len(row)
    nullCount = 0
    for i in range(0, totalLength):
        if "nan" == str(row[i]):
            nullCount += 1
    
    if nullCount == totalLength:
        return True
    else:
        return False

def TransformExcel():
    count = 0
    # get the column
    while True:
        column = input("Inserisci il carattere della colonna che vuoi usare nel filtro\n")
        if len(column) == 1:
            column = ord(column.lower()) - 97
            # print(column)
            break
        
    #get the filter and the column type
    _filter = input("Inserisci il filtro\n")
    try:
        _filter = int(_filter)
        columnType = int
    except:
        columnType = string
        
    print(type(_filter))

    for i in range(0, len(file)):
        if CheckNullRow(file[i]) == False:
            find = None
            if columnType == int:
                try:
                    find = int(file[i][column])
                except:
                    pass
            else:
                find = file[i][column]
            
            if find == _filter:
                rows.append(i)
                count += 1
        else:
            rows.append(i)

    print(f"Trovate {count} righe corrispondenti al tuo filtro")

# read the excel file
while True:
    try:
        fileName = input("Inserisci il nome del file\n") + ".xlsx"
        file = pd.read_excel(fileName, header=None)
        file = file.to_numpy()
        fileExist = True
    except KeyboardInterrupt:
        exit(1)
    except:
        print("il file non esiste\n")
    if fileExist == True:
        break
    
TransformExcel()

while True:
    ris = input("Vuoi applicare altri filtri? [yes/no] ").lower()
    if ris == "yes":
        TransformExcel()
    else:
        break

answ = input("Vuoi salvare il file? [yes/no]: ").lower()
if answ == 'yes':
    ## convert your array into a dataframe
    df = pd.DataFrame(file)
    # delete rows corresponding to the value of each array's element
    df = df.drop(rows)
    # save to xlsx file
    df.to_excel('output.xlsx', index=False, header = False)
    
    """
    # Print all first row
    print(df.loc[0,:])
    
    # Convert first row to json
    ciao = df.loc[0,:].to_json()
    print(ciao)
    """