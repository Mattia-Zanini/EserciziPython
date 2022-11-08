nameFile = str(input("Inserisci il nome e formato del file\n"))

f = open(nameFile, "r", encoding="utf-8")
file = []
importValues = []

index = 0
fields = {}
keysNames = []

def RemoveChars(l):
    l = l.replace("\n", "")
    return l


def Format(l):
    sL = l.split(",")
    return sL


def CountChars(sL, par, c):
    for i in range(0, len(sL)):
        if c < len(sL[par]):
            c = len(sL[par])
    return c

def GetMaxLength(p):
    cc = 0
    for i in range(0, len(file)):
        cc = CountChars(file[i], p, cc)
    return cc


for line in f:
    if index != 0:
        line = RemoveChars(line)
        singleLine = Format(line)
        file.append(singleLine)
    else:
        line = RemoveChars(line)
        singleLine = Format(line)
        
        for i in range(0, len(singleLine)):
            fields[str(singleLine[i])] = None
        
        for key in fields.keys():
            keysNames.append(key)

    index += 1

print("\n")

for i in range(0, len(fields)):
    print(f"{keysNames[i]}: max_length: {GetMaxLength(i)}")