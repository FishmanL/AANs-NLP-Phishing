import csv
csvfile = open('dataset1', 'r').readlines()
filename1 = "TrainingData"
filename2="TestingData"
x=len(csvfile)*4/5
x=round(x)
print(x)
i=0
open(str(filename1) + '.csv', 'w+').writelines(csvfile[i:x])
i=2138
open(str(filename2) + '.csv', 'w+').writelines(csvfile[i:len(csvfile)])
i+=x*.25
print(len(csvfile))
print(i)