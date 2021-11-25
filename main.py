def obrada(string1):
    stringStart = ""
    stringEnd = ""
    for i in range(0, 12):
        stringStart += string1[i]
    for i in range(17, len(string1)):
        stringEnd += string1[i]

    strAdd = "01:41:07,920"
    hAdd = int(strAdd[:2])
    mAdd = int(strAdd[3:5])
    sAdd = int(strAdd[6:8])
    oAdd = int(strAdd[9:])
    addItems = []
    addItems.append(hAdd)
    addItems.append(mAdd)
    addItems.append(sAdd)
    addItems.append(oAdd)

    stringStart = stringStart.split(':')
    stringStart2 = stringStart[2].split(',')
    stringStart.pop()
    for item in stringStart2:
        stringStart.append(item)
    for i in range(len(stringStart)):
        stringStart[i] = int(stringStart[i])

    stringEnd = stringEnd.split(':')
    stringEnd2 = stringEnd[2].split(',')
    stringEnd.pop()
    for item in stringEnd2:
        stringEnd.append(item)
    for i in range(len(stringEnd)):
        stringEnd[i] = int(stringEnd[i])

    for i in range(len(addItems)):
        stringStart[i] += addItems[i]
        stringEnd[i] += addItems[i]


    stringStart[2] += int(stringStart[3] / 1000)
    stringStart[3] = stringStart[3] % 1000
    stringStart[1] += int(stringStart[2] / 60)
    stringStart[2] = stringStart[2] % 60
    stringStart[0] += int(stringStart[1] / 60)
    stringStart[1] = stringStart[1] % 60

    stringEnd[2] += int(stringEnd[3] / 1000)
    stringEnd[3] = stringEnd[3] % 1000
    stringEnd[1] += int(stringEnd[2] / 60)
    stringEnd[2] = stringEnd[2] % 60
    stringEnd[0] += int(stringEnd[1] / 60)
    stringEnd[1] = stringEnd[1] % 60

    s = ""
    for i in range(len(stringStart)):
        if stringStart[i] < 10:
            s += "0" + str(stringStart[i])
        else:
            s += str(stringStart[i])
        s += ":"
    n = len(s)
    s = s[:n - 1]
    stringStart = s.split(':')
    s = ""
    s += stringStart[0] + ":" + stringStart[1] + ":" + stringStart[2] + "," + stringStart[3]
    stringStart = s
    s = ""
    for i in range(len(stringEnd)):
        if stringEnd[i] < 10:
            s += "0" + str(stringEnd[i])
        else:
            s += str(stringEnd[i])
        s += ":"
    n = len(s)
    s = s[:n - 1]
    stringEnd = s.split(':')
    s = ""
    s += stringEnd[0] + ":" + stringEnd[1] + ":" + stringEnd[2] + "," + stringEnd[3]
    stringEnd = s
    stringRes = stringStart + " --> " + stringEnd
    return stringRes

with open('avcdvd-hamlet.2009.dvdrip.xvid-cd2.srt', 'r') as f:
    data = f.readlines()

for i in range(len(data)):
    line = data[i]
    if "-->" in line:
        line = obrada(line)
        line += "\n"
        data[i] = line
print(data)

with open('test.txt', 'w') as file:
    for line in data:
        file.write(line)
