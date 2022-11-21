from cmath import inf
from math import nan
import string
import pandas as pd
import os
def clear(): return os.system('cls')


# clear()


class DataPositions:
    # This is a class for keeping track of the positions
    id_array = []
    codice_parrocchia_array = []
    long_array = []
    long2_array = []
    lat_array = []
    lat2_array = []


# place "r" before the path string to address special character, such as '\'.
# Don't forget to put the file name at the end of the path + '.xlsx'
pd.set_option('display.max_rows', 1000)
df = pd.read_excel(r'posizioni.xlsx')

data = DataPositions()

data.id_array = df['id'].to_numpy()
data.codice_parrocchia_array = df['codice_parrocchia'].to_numpy().astype(int)
data.long_array = df['long'].to_numpy()
data.long2_array = df['long2'].to_numpy()
data.lat_array = df['lat'].to_numpy()
data.lat2_array = df['lat2'].to_numpy()

# print(data.lat_array)
# print(data.lat_array[381])
# print(pd.isna(data.lat_array[381]))  # controlla se il valore è nan

"""
logitudine = str(data.long_array[0]) + "." + str(int(data.long2_array[0]))
latitudine = str(int(data.lat_array[0])) + "." + str(int(data.lat2_array[0]))
print(logitudine + "\n" + latitudine)
"""


dataExcel = []
for i in range(len(data.id_array)):
    arr = []
    arr.append(data.id_array[i])
    arr.append(data.codice_parrocchia_array[i])

    logitudine = ""
    latitudine = ""

    # controllo se il valore della longitutine è valido
    if pd.isna(data.long_array[i]) == False and pd.isna(data.long2_array[i]) == False:
        logitudine = str(
            int(data.long_array[i])) + "." + str(int(data.long2_array[i]))

    # controllo se il valore della latitudine è valido
    if pd.isna(data.lat_array[i]) == False and pd.isna(data.lat2_array[i]) == False:
        latitudine = str(int(data.lat_array[i])) + \
            "." + str(int(data.lat2_array[i]))

    if logitudine != "":
        arr.append(float(logitudine))
    else:
        arr.append(logitudine)

    if latitudine != "":
        arr.append(float(latitudine))
    else:
        arr.append(latitudine)

    dataExcel.append(arr)


print(dataExcel[0])


"""
df1 = pd.DataFrame(
    [['a', 'b'], ['c', 'd']],
    index=['row 1', 'row 2'],
    columns=['col 1', 'col 2']
)
df1.to_excel("output.xlsx")
"""


# da togliere alla fine
df = pd.DataFrame(dataExcel, columns=[
                  'id', 'codice_parrocchia', 'longitudine', 'latitudine'])

df.to_excel('PosPython.xlsx', index=False)
