import pandas as pd
import numpy as np
import string
import openpyxl

# place "r" before the path string to address special character, such as '\'.
# Don't forget to put the file name at the end of the path + '.xlsx'

file = pd.read_excel(r'my_file.xlsx', header=None)
file = file.to_numpy()

count = 0
rows = []

for i in range(0, len(file)):
    parola = None
    try:
        parola = str(file[i][7])
        # print(n)
        if parola == "ITS15":
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
filepath = 'my_file2.xlsx'
#df.to_excel(filepath, index=False)