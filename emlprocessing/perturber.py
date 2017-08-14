import spamcheck
import email
import os
#NEXT STEPS:  TRY PERTURBATIONS MANUALLY, THEN SET UP AUTOMATIC TESTING OF DELTA SPAM

#perturbation function: currently just modifying commonly used words
def perturb(x):
    y=x
    #service modification
    if 'penis' in x or 'Penis' in x or 'PENIS' in x:
      y=y.replace('penis', 'pemis')
      y=y.replace('Penis', 'Pemis')
      y=y.replace('PENIS', 'PEMIS')
    if 'drugs' in x or 'Drugs' in x or 'DRUGS' in x:
        y = y.replace('drugs ', 'dr ugs')
        y = y.replace('Drugs ', 'Dr ugs')
        y = y.replace('DRUGS ', 'DR UGS')
    if 'body' in x or 'Body' in x or 'BODY' in x:
      y=y.replace('body', 'bod')
      y=y.replace('Body', 'Bod')
      y=y.replace('BODY', 'BOD')
    #Funds modification
    if 'money' in x or 'Money' in x or 'MONEY' in x:
      y=y.replace('money ', 'mo ney')
      y=y.replace('Money ', 'Mo ney')
      y=y.replace('MONEY ', 'MO NEY')

    if 'dollars' in x or 'Dollars' in x or 'DOLLARS' in x:
      y=y.replace('dollars', 'doIIars')
      y=y.replace('Dollars', 'DoIIars')
      y=y.replace('DOLLARS', 'DOIIARS')
    if 'guarantee' in x or 'Guarantee' in x or 'GUARANTEE' in x:
      y=y.replace('guarantee ', 'guaran tee')
      y=y.replace('Guarantee ', 'Guaran tee')
      y=y.replace('GUARANTEE ', 'GUARAN TEE')
    if 'form' in x or 'Form' in x or 'FORM' in x:
      y=y.replace('form ', 'fo rm')
      y=y.replace('Form ', 'Fo rm')
      y=y.replace('FORM ', 'FO RM')
    if 'quote' in x or 'Quote' in x or 'QUOTE' in x:
      y=y.replace('quote', 'quo te')
      y=y.replace('Quote', 'Quo te')
      y=y.replace('QUOTE', 'QUO TE')
    if 'buy' in x or 'Buy' in x or 'BUY' in x:
      y=y.replace('buy ', 'bu y')
      y=y.replace('Buy ', 'Bu y')
      y=y.replace('BUY ', 'BU Y')
    if 'credit' in x or 'Credit' in x or 'CREDIT' in x:
      y=y.replace('credit', 'cred')
      y=y.replace('Credit', 'Cred')
      y=y.replace('CREDIT', 'CRED')
    if 'lott' in x or 'Lott' in x or 'LOTT' in x:
      y=y.replace('lott', 'lo tt ')
      y=y.replace('Lott', 'Lo tt ')
      y=y.replace('LOTT', 'LO TT ')
    if 'offer' in x or 'Offer' in x or 'OFFER' in x:
      y=y.replace('offer ', 'of fer')
      y=y.replace('Offer ', 'Of fer')
      y=y.replace('OFFER ', 'OF FER')
    if 'price' in x or 'Price' in x or 'PRICE' in x:
        y = y.replace('price', 'amount')
        y = y.replace('Price', 'Amount')
        y = y.replace('PRICE', 'AMOUNT')
    if 'remove' in x or 'Remove' in x or 'REMOVE' in x:
        y = y.replace('remove ', 'rem ove')
        y = y.replace('Remove ', 'R emove')
        y = y.replace('REMOVE ', 'REM OVE')
    #elimination of problematic phrases
    if 'dear' in x or 'Dear' in x or 'DEAR' in x:
        y = y.replace('dear', '')
        y = y.replace('Dear', '')
        y = y.replace('DEAR', '')
    if 'this ad' in x or 'This ad' in x or 'This Ad' in x:
        y = y.replace('this ad', 'this')
        y = y.replace('This ad', 'This')
        y = y.replace('This Ad', 'This')

    return y
#initializing necessary variables-iterator through the eml files, average perturbation score, and the file list
n=0
k=0
avgdelperturb=0
files=os.listdir(".\Testing")
while n<len(files):
    #pick the specific file
    file=files[n]
    filename, ext=os.path.splitext(file)
    #read the file, only bother testing it's perturbation if it's spam
    if ext==".eml" and file[3]!='1':
        filenamenew='.\Testing\\'+file
        filename=open(filenamenew, "r", encoding='Windows-1252')
        print('starting')
        f=filename.read()
        #call the spamcheck API
        result = spamcheck.check(f, report=True)
        print('spam checked')
        if 'score' in result.keys():
            score = result['score']
            report = result['report']
        else:
            score=0

        #perturb, then call again
        g=perturb(f)
        #print(str(g))
        result = spamcheck.check(g, report=True)
        print('perturbed checked')
        if 'score' in result.keys() and float(score) >0.0:
            scorep = result['score']
            reportp = result['report']
        else:
            scorep=score
        #get the changes, then print metrics
        delscore=float(score)-float(scorep)

        avgdelperturb+=delscore
        print(str(file) + ":")
        print(str(score))
        print(str(report))
        if delscore<0.0:
            print(str(reportp))
        print(str(delscore))
    n+=1
    k+=1
    #stop every so often to check progress(more necessary if scores and reports are unprinted)
    if k%10==0:
        print(str(k)+ ' files processed...')
        print('Current average:' + str(avgdelperturb / k))


avgdelperturb=avgdelperturb/k
print(avgdelperturb)