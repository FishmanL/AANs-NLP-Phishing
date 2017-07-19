import csv
import random
#this combines 5 csv files of perturbed data and one of nonperturbed data into one dataset for perturbation detection
# replace placeholders with desired perturbed files
file1="attackfile2deh.csv"
file2="attackfile8.csv"
file3="attackfile8cdeh.csv"
file4="attackfile58ehj.csv"
file5="attackfile3.csv"
file6="attackfile2.csv"
file7="attackfile5ach.csv"
file8="attackfile8.csv"
file9="attackfile8f.csv"
file10="attackfile58ehj.csv"
normal="TrainingData1.csv"
def shuffle(source, target):
    with open(source, 'r') as source:
        data = [(random.random(), line) for line in source]
    data.sort()
    with open(target, 'w+') as target:
        for _, line in data:
            target.write(line)
#shuffle all files
shuffle(file1, "file1shuffle.csv")
shuffle(file2, "file2shuffle.csv")
shuffle(file3, "file3shuffle.csv")
shuffle(file4, "file4shuffle.csv")
shuffle(file5, "file5shuffle.csv")
shuffle(file6, "file6shuffle.csv")
shuffle(file7, "file7shuffle.csv")
shuffle(file8, "file8shuffle.csv")
shuffle(file9, "file9shuffle.csv")
shuffle(file10, "file10shuffle.csv")
shuffle(normal, "trainingshuffle.csv")
#label all files correctly(1 is perturbed, 0 is nonperturbed)
r = csv.reader(open('file6shuffle.csv')) # Here your csv file
lines6 = [l for l in r]
for line in lines6:
    if len(line)!=0:
        lineindex=len(line)-1

        line[lineindex]=1

r = csv.reader(open('file7shuffle.csv')) # Here your csv file
lines7 = [l for l in r]
for line in lines7:
    if len(line)!=0:
        lineindex=len(line)-1

        line[lineindex]=1

r = csv.reader(open('file8shuffle.csv')) # Here your csv file
lines8 = [l for l in r]
for line in lines8:
    if len(line)!=0:
        lineindex=len(line)-1

        line[lineindex]=1

r = csv.reader(open('file9shuffle.csv')) # Here your csv file
lines9 = [l for l in r]
for line in lines9:
    if len(line)!=0:
        lineindex=len(line)-1

        line[lineindex]=1

r = csv.reader(open('file10shuffle.csv')) # Here your csv file
lines10 = [l for l in r]
for line in lines10:
    if len(line)!=0:
        lineindex=len(line)-1
        line[lineindex]=1
r = csv.reader(open('file1shuffle.csv')) # Here your csv file
lines1 = [l for l in r]
for line in lines1:
    if len(line)!=0:
        lineindex=len(line)-1

        line[lineindex]=1

r = csv.reader(open('file2shuffle.csv')) # Here your csv file
lines2 = [l for l in r]
for line in lines2:
    if len(line)!=0:
        lineindex=len(line)-1
        line[lineindex]=1

r = csv.reader(open('file3shuffle.csv')) # Here your csv file
lines3 = [l for l in r]
for line in lines3:
    if len(line)!=0:
        lineindex=len(line)-1
        line[lineindex]=1

r = csv.reader(open('file4shuffle.csv')) # Here your csv file
lines4 = [l for l in r]
for line in lines4:
    if len(line)!=0:
        lineindex=len(line)-1

        line[lineindex]=1

r = csv.reader(open('file5shuffle.csv')) # Here your csv file
lines5 = [l for l in r]
for line in lines5:
    if len(line)!=0:
        lineindex=len(line)-1
        line[lineindex]=1

r = csv.reader(open('trainingshuffle.csv')) # Here your csv file
linest = [l for l in r]
print(len(linest))
test=0
for line in linest:
    if len(line)!=0:
        test+=1
        lineindex=len(line)-1
        line[lineindex]=0
print(test)

#combine all files into one
lines1.extend(lines2)
print(len(lines1))
lines1.extend(lines3)
print(len(lines1))
lines1.extend(lines4)
lines1.extend(lines5)
lines1.extend(lines6)
lines1.extend(lines7)
lines1.extend(lines8)
lines1.extend(lines9)
lines1.extend(lines10)
lines1.extend(linest)
print(len(lines1))

pfile=open('perturbmain.csv', 'w+')
writer=csv.writer(pfile)
test=0
for row in lines1:
    if len(row)>0:
        test+=1
        writer.writerow(row)
print(test)
#reshuffle the final file, then separate into training and test data
shuffle('perturbmain.csv', 'perturbshuffle.csv')
csvfile = open('perturbshuffle.csv', 'r').readlines()
filename1 = "PerturbTrainingData"
filename2="PerturbTestingData"
x=len(csvfile)*4/5
x=round(x)

i=0
open(str(filename1) + '.csv', 'w+').writelines(csvfile[i:x])
i=x
open(str(filename2) + '.csv', 'w+').writelines(csvfile[i:len(csvfile)])
i+=x*.25



