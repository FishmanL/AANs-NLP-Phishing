import csv
#full list of perturbations possible for an attacker on the huddersfield featureset
bitflippedguide1=[0, 1, 2, 3, 4, 5, 19, 7, 9, 11, 12, 13, 14, 16, 17, 18, 20, 21, 22, 29]
#shrunken list of perturbations(realistic list)
bitflippedguide=[ 1, 2, 4, 7, 9, 11, 12, 13, 14, 16, 17, 18, 29]
#finds all subsets of a given list
def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + y for y in x]
#create all possible perturbations
bitflippedlist=subs(bitflippedguide)
namearray=[]
#this next function does the actual perturbation--for each possible perturbation it generates a perturbed version of the huddersfield-based test set
r = csv.reader(open('TestingData1.csv'))
lines = [l for l in r]
for y in bitflippedlist:
    #the perturbation portion
    for line in lines:
        for x in y:
            line[x]=1
    #naming the perturbed file for easy retrieval/output
    name = ""
    namestring="123456789abcdefghijklmnopqrstuv"

    for x in y:
        name=name+namestring[x]
    name="attackfile" + name + ".csv"
    namearray.append(name)
    print(name)
    print(namearray)
    writer = csv.writer(open(name, 'w'))
    writer.writerows(lines)
