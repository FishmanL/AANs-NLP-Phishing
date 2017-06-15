import csv
bitflippedguide1=[0, 1, 2, 3, 4, 5, 19, 7, 9, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 29]
bitflippedguide=[ 1, 2, 4, 7, 9, 11, 12, 13, 14, 16, 17, 18, 29]
def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + y for y in x]
bitflippedlist=subs(bitflippedguide)
bitflipped=[0, 1, 2, 4, 7, 9, 11, 12, 13, 14, 16, 17, 18, 20 ]
r = csv.reader(open('TestingData1.csv')) # Here your csv file
lines = [l for l in r]
for y in bitflippedlist:
    for line in lines:
        for x in y:
            line[x]=1
    name = ""
    namestring="123456789abcdefghijklmnopqrstuv"
    for x in y:
        name=name+namestring[x]
    name="attackfile" + name + ".csv"
    print(name)
    writer = csv.writer(open(name, 'w'))
    writer.writerows(lines)
