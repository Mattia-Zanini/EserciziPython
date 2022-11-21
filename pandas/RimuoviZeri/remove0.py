import pandas as pd
import numpy as np
import string
import openpyxl

# place "r" before the path string to address special character, such as '\'.
# Don't forget to put the file name at the end of the path + '.xlsx'

file = pd.read_excel(r'bollato.xlsx', header=None)
file = file.to_numpy()

count = 0
rows = []


for i in range(0, len(file)):
    n = ""
    try:
        n = int(file[i][9])
        # print(n)
        if n == 0:
            # print(file[i])
            # file = np.delete(file, i)
            rows.append(i)
            count = count + 1
    except:
        pass

print(count)


## convert your array into a dataframe
df = pd.DataFrame(file)
df = df.drop(rows)
## save to xlsx file
filepath = 'my_file.xlsx'
#df.to_excel(filepath, index=False)