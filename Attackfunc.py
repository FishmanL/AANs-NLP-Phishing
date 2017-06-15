import csv
bitflipped=[ 1, 2, 4, 7]
r = csv.reader(open('TestingData1.csv')) # Here your csv file
lines = [l for l in r]
for line in lines:
	for x in bitflipped:
		line[x]=1
name = ""
for x in bitflipped:
    name=name+str(x+1)
name="attackfile" + name + ".csv"
print(name)
writer = csv.writer(open(name, 'w'))
writer.writerows(lines)
