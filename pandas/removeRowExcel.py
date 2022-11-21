import pandas as pd
import numpy as np
import string
import openpyxl

rows = []
file = []
count = 0
fileExist = False
fileName = None
column = None
columnType = int

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

print(f"Trovate {count} righe corrispondenti al tuo filtro")

answ = input("Vuoi salvare il file? [yes]/[no]: ").lower()
if answ == 'yes':
    ## convert your array into a dataframe
    df = pd.DataFrame(file)
    # delete rows corresponding to the value of each array's element
    df = df.drop(rows)
    # save to xlsx file
    filepath = 'output.xlsx'
    df.to_excel(filepath, index=False)