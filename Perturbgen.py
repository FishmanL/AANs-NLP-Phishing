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
        y = unshorten_url(y)
        y = y[2:]
    j = ''
    z = ''
    savehttp = ''

    # savehttp gets http or https, purge for the rest of the string
    if x[4] == 's':
        savehttp = x[:8]
        j = y[8:]
        y = j
    elif x[4] == ':':
        savehttp = x[:7]
        j = y[7:]
        y = j
    # kill @ symbol
    if '4' in key:
        if '@' in y:
            print(y.index('@'))
            y = y[y.index('@') - 1:]
    if '5' in key:
        if '//' in y:
            print(y.index('//'))
            y = y[y.index('//') + 2:]
    # get rid of the IP for getting domains/redirections, domarray holds all theoretical subdomains, redirarray holds all slashed out pieces, redirdom holds all domains before slashes
    iptest = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', y)
    noip = re.sub('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '', y)
    domarray = [x for x in map(str.strip, noip.split('.')) if x]
    redirarray = [x for x in map(str.strip, noip.split('/')) if x]
    z = redirarray[0]
    redirdom = [z for z in map(str.strip, z.split('.')) if z]
    # purge dashes
    if '6' in key:
        print(redirdom)
        for i in range(len(redirdom)):
            if '-' in redirdom[i]:
                redirdom[i] = redirdom[i].replace('-', '')
        y = redirdom[0]
        for i in redirdom:
            if i == redirdom[0]:
                continue
            y += ('.' + i)
        for i in redirarray:
            if i == redirarray[0]:
                continue
            y += ('/' + i)
        noip = re.sub('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '', y)
        domarray = [x for x in map(str.strip, noip.split('.')) if x]
        redirarray = [x for x in map(str.strip, noip.split('/')) if x]
    # purge https
    if '8' in key:
        print(redirdom)
        for i in range(len(redirarray)):
            if 'https' in redirarray[i]:
                redirarray[i] = redirarray[i].replace('https', '')
        y = redirarray[0]
        for i in redirarray:
            if i == redirarray[0]:
                continue
            y += ('/' + i)
        noip = re.sub('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', '', y)
        domarray = [x for x in map(str.strip, noip.split('.')) if x]
        z = redirarray[0]
        redirdom = [z for z in map(str.strip, z.split('.')) if z]
    # get prefix and suffix for URL
    pref = redirdom[0]
    preflen = len(pref)
    suff = redirdom[len(redirdom) - 1]
    sufflen = len(suff)

    # kill subdomains
    if '7' in key and len(redirdom) > 3:
        y = pref + "." + redirdom[1] + "." + suff
        for i in redirarray:
            if i == redirarray[0]:
                continue
            y += ('/' + i)
    # kill IP
    if '1' in key and iptest:
        y = str(redirarray[1]) + ".com"
    # shrink URL
    if '2' in key and len(x) > 30:
        # long URL, get first domain and first subdomain
        if len(redirdom) >= 3 and len(redirarray) >= 2:
            y = str(redirdom[0]) + "." + str(redirdom[1]) + "." + str(redirdom[len(redirdom) - 1]) + '/' + str(
                redirarray[len(redirarray) - 1])
        if len(y) > 30 and len(redirdom) >= 3:
            y = str(redirdom[0]) + "." + str(redirdom[1]) + "." + str(redirdom[len(redirdom) - 1])
        if len(y) > 30:
            y = str(redirdom[0]) + "." + str(redirdom[1])
    #makedomain https
    if 'c' in key:
        savehttp="https://"
    y = savehttp + y
    return y


y = "http://www.weare-atest.google.microsoftweswearhttps.com/testingallthethingshttps/whyarewetestingthis"

print(perturb(y, 'c'))
