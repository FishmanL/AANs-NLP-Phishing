import os
files=os.listdir(".\kappa\kappa")
length=200
#the below is likely unnecessary
space=" "
namelen=len(files[1])
filenames=space.join(files)
def getnameatlen(string, index, len):
    point=len*index
    str=string[point:point+len]
    return str

tp=0.0
tn=0.0
fp=0.0
fn=0.0
y1=0.0
y2=0.0
n1=0.0
n2=0.0
n=0
k=len(files)
while n<int(k/2)-1:
    name1=files[n]
    name2=files[n+int(k/2)]
    if name1[5]!='1':
        y1+=1.0
    else:
        n1+=1.0
    if name2[5]!='1':
        y2+=1.0
    else:
        n2+=1.0
    if name1[5]==name2[5] and name1[5]=='1':
        tn+=1.0
    elif name1[5]==name2[5] and name1[5]!='1':
        tp+=1.0
    elif name1[5]!=name2[5] and name1[5]=='1':
        fp+=1.0
    elif name1[5]!=name2[5] and name1[5]!='1':
        fn+=1.0
    n+=1
obsagreement=(tp+tn)/100.0
probyes=y1/100.0*y2/100.0
probno=n1/100.0*n2/100.0
expectedprob=probyes+probno
kappa = (obsagreement - expectedprob) / (1.0 - expectedprob)
print(str(kappa))
print(str(tp))
print(str(tn))
print(str(fp))
print(str(fn))