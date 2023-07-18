def Format(l):
    sL = l.split('"')
    # print(sL)
    return sL


def WriteString(sL, isCSS):
    string = ""
    if isCSS == True:
        string = f"wp_enqueue_style('CDN', \"{sL[1]}\", array(), '1.0', 'all');"
    else:
        string = f"wp_enqueue_script('CDN', \"{sL[1]}\", array(), '1.0', true);"
    return string


f = open("cdn.txt", "r", encoding="utf-8")
lines = []

for line in f:
    singleLine = Format(line)
    lines.append(WriteString(singleLine, True))

with open("export.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(f"{line}\n")
