import os
import re
import pycurl
import requests

def unshorten_url(url):
    return requests.head(url, allow_redirects=True).url
def perturb(x, key):
    y = x
    # replace IP
    if '3' in key:
        y=unshorten_url(y)
        y=y[2:]
    # kill @ symbol
    if '4' in key:
        if '@' in y:
            print(y.index('@'))
            y=y[y.index('@')-1:]
    j=''
    z=''
    savehttp=''

    #savehttp gets http or https, purge for the rest of the string
    if x[4]=='s':
        savehttp=x[:8]
        j=y[8:]
        y=j
    elif x[4]==':':
        savehttp = x[:7]
        j=y[7:]
        y=j
    #get rid of the IP for getting domains/redirections, domarray holds all theoretical subdomains, redirarray holds all slashed out pieces, redirdom holds all domains before slashes
    noip= re.sub('\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', '', y)
    domarray=[x for x in map(str.strip, noip.split('.')) if x]
    redirarray = [x for x in map(str.strip, noip.split('/')) if x]
    z=redirarray[0]
    redirdom = [z for z in map(str.strip, z.split('.')) if z]
    #get prefix and suffix for URL
    pref=redirdom[0]
    preflen=len(pref)
    suff=redirdom[len(redirdom)-1]
    sufflen=len(suff)



    #kill IP
    if '1' in key:
        y=noip
    #shrink URL
    if '2' in key and len(x)>30:
        #long URL, get first domain and first subdomain
        if len(redirdom)>=3 and len(redirarray)>=2:
            y=savehttp+str(redirdom[0])+"."+str(redirdom[1])+"."+str(redirdom[len(redirdom)-1])+'/'+str(redirarray[len(redirarray)-1])
        if len(y)>30:
            y = savehttp + str(redirdom[0]) + "." + str(redirdom[1]) + "." + str(redirdom[len(redirdom) - 1])

    return y

y="https://test.testerly.testingtesting.tryhard/123456"

print(perturb(y, '124'))
