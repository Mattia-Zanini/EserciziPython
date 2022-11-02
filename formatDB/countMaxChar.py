f = open("elenco.txt", "r", encoding="utf-8")
file = []
importValues = []
count = 0


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


for line in f:
    line = RemoveChars(line)
    singleLine = Format(line)
    param = 6
    count = CountChars(singleLine, param, count)

print("Questo è il numero massimo di char: " + str(count))
