import email
import os
from bs4 import BeautifulSoup
import base64
import re
#gets the text and from line from EML
filepos="PositiveExamples.txt"
fileneg="NegativeExamples.txt"

f=os.listdir(".\Testing")
n=len(f)
print(str(n)+"\r\n")
n=0
while n<len(f):
    file=f[n]
    filename, ext=os.path.splitext(file)
    if ext==".eml":
        filenamenew='.\Testing\\'+file
        filename=open(filenamenew, "r", encoding='Windows-1252')
        msg=email.message_from_file(filename)
        msgstring=msg.get_payload()
        if(len(msgstring))>1 and isinstance(msgstring, str)==False:
            msgstring=msgstring[0]
        msgstring=str(msgstring)
        msgstring.replace('\n', ' ')
        msgstring.replace('\r', ' ')
        if msgstring.find("X-B")!=-1 or msgstring.find("X-P")!=-1:
            print("Problem string, email: " + file + "\r\n")
        if msgstring.find('Content-Transfer-Encoding: base64')!=-1:
            print(file + " contains base64 \r\n")
        msgfrom=msg.get('From')
        msgsubject=msg.get('Subject')
        if file[3]=="1":
            fn = open(fileneg, "a+")
            fn.write(str(msgstring)+"\r\n")
            fn.write("//////"+"\r\n")
            fn.close()
        else:
            fp = open(filepos, "a+")
            fp.write(str(msgstring) + "\r\n")
            fp.write("//////" + "\r\n")
            fp.close()

    n+=1
    print(str(n)+ " files processed...\r\n")