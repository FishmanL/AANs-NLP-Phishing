import random
with open('dataset.csv','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('dataset1','w') as target:
    for _, line in data:
        target.write( line )