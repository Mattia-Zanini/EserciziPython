nameFile = str(input("Inserisci il nome e formato del file\n"))

f = open(nameFile, "r", encoding="utf-8")
file = []
importValues = []

def RemoveChars(l):
    l = l.replace('\n', "")
    l = l.replace(' ', "")
    return l


def Format(l, char):
    sL = l.split(char)

    for i in range(0, len(sL)):
        if sL[i] == "NULL":
            sL[i] = None

    return sL


def WriteString(sL):
    string = ""
    for i in range(0, 7):
        if i < 6:
            string += str(sL[i]) + ","
        else:
            string += str(sL[i])

    return string


for line in f:
    line = RemoveChars(line)
    singleLine = Format(line, ',')
    
    if len(importValues) != 0:
        for i in range(0, 2):
            date = Format(singleLine[i], '/')
            singleLine[i] = f"{str(date[2])}/{str(date[1])}/{str(date[0])}"
        
    #print(singleLine)
    # file.append(singleLine)
    importValues.append(WriteString(singleLine))


with open('your_file.csv', "w", encoding='utf-8') as f:
    for line in importValues:
        f.write(f"{line}\n")