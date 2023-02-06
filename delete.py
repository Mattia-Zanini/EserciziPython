lines = []

with open("ConsoleHost_history.txt") as file_in:
    for line in file_in:
        lines.append(line.strip())
        #lines.append(line)

lines = list(set(lines))

print(lines)

file = open('backupPowershellCommands.txt','w')
for item in lines:
	file.write(item+"\n")
file.close()