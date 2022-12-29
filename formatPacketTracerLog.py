def RemoveChars(l):
    l = l.replace("\n", "")
    return l


def Format(l):
    sL = l.split(" ")
    sL = [i for i in sL if i != ""]
    print(sL)
    return sL


def WriteString(sL):
    string = ""
    for i in range(6, len(sL)):
        if i == len(sL) - 1:
            string += sL[i]
        else:
            string += sL[i] + " "
    return string


f = open("C:\\Users\\mattz\\Desktop\\export.txt", "r", encoding="utf-8")
importValues = []

for line in f:
    line = RemoveChars(line)
    singleLine = Format(line)
    importValues.append(WriteString(singleLine))


with open("C:\\Users\\mattz\\Desktop\\your_file.txt", "w", encoding="utf-8") as f:
    for line in importValues:
        f.write(f"{line}\n")
