import csv
import random
file1="placeholder"
file2="placeholder"
file3="placeholder"
file4="placeholder"
file5="placeholder"
normal="TrainingData1.csv"
def shuffle(source, target):
    with open(source, 'r') as source:
        data = [(random.random(), line) for line in source]
    data.sort()
    with open(target, 'w+') as target:
        for _, line in data:
            target.write(line)
shuffle(file1, "file1shuffle.csv")
shuffle(file2, "file2shuffle.csv")
shuffle(file3, "file3shuffle.csv")
shuffle(file4, "file4shuffle.csv")
shuffle(file5, "file5shuffle.csv")
shuffle(normal, "trainingshuffle.csv")
r = csv.reader(open('file1shuffle.csv')) # Here your csv file
lines1 = [l for l in r]
for line in lines1:
    line[-1]=1

r = csv.reader(open('file2shuffle.csv')) # Here your csv file
lines2 = [l for l in r]
for line in lines2:
    line[-1]=1

r = csv.reader(open('file3shuffle.csv')) # Here your csv file
lines3 = [l for l in r]
for line in lines3:
    line[-1]=1

r = csv.reader(open('file4shuffle.csv')) # Here your csv file
lines4 = [l for l in r]
for line in lines4:
    line[-1]=1

r = csv.reader(open('file5shuffle.csv')) # Here your csv file
lines5 = [l for l in r]
for line in lines5:
    line[-1]=1

r = csv.reader(open('trainingshuffle.csv')) # Here your csv file
linest = [l for l in r]
for line in linest:
    line[-1]=0
linesmain=lines1.extend(lines2).extend(lines3).extend(lines4).extend(lines5).extend(linest)
open('perturbmain.csv', 'w+').writelines(linesmain)
csvfile = open('perturbmain.csv', 'r').readlines()
filename1 = "PerturbTrainingData"
filename2="PerturbTestingData"
x=len(csvfile)*4/5
x=round(x)
print(x)
i=0
open(str(filename1) + '.csv', 'w+').writelines(csvfile[i:x])
i=x
open(str(filename2) + '.csv', 'w+').writelines(csvfile[i:len(csvfile)])
i+=x*.25
print(len(csvfile))
print(i)


