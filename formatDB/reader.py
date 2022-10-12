f = open("elenco.txt", "r", encoding='utf-8')
file = []
importValues = []


def RemoveChars(l):
    l = l.replace('\n', "")
    l = l.replace(' ', "")
    return l


def Format(l):
    sL = l.split(',')

    for i in range(0, len(sL)):
        if sL[i] == "NULL":
            sL[i] = None

    return sL


def WriteString(sL):
    string = "("
    for i in range(0, len(sL)):
        if i < len(sL) - 1:
            string += "'" + str(sL[i]) + "',"
        else:
            string += "'" + str(sL[i]) + "'),"

    return string


for line in f:
    line = RemoveChars(line)
    singleLine = Format(line)
    # file.append(singleLine)

    importValues.append(WriteString(singleLine))


with open('your_file.txt', "w", encoding='utf-8') as f:
    for line in importValues:
        f.write(f"{line}\n")
