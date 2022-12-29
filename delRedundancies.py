defaultOutputPath = "C:\\Users\\mattz\\Desktop\\your_file.txt"
file = []
toWrite = []

pathFile = input("Inserisci il nome del file o il percorso\n")
f = open(pathFile, "r", encoding="utf-8")

try:
    f = open(pathFile, "r", encoding="utf-8")
except OSError:
    print(f"Could not open/read file: {pathFile}\n")
    exit()

def RemoveChars(l):
    l = l.replace("\n", "")
    return l

# read all file lines
for row in f:
    row = RemoveChars(row)
    file.append(row)
    
print(f"Lines pre-delete redundancies: {len(file)}")

file2 = set(file)
toWrite = list(file2)

with open(defaultOutputPath, "w", encoding="utf-8") as f:
    for line in toWrite:
        f.write(f"{line}\n")

print(f"Lines after-delete redundancies: {len(toWrite)}")
print("Completed writing")