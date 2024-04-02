# -*- coding: utf-8 -*-
import re
ffile=input("please enter the path to your file \n>>>")
myfile=open(ffile,'r')

regex="New Revision: (\d+)"
#flist=list()
summed=float()
counter=0
for line in myfile:
    line=line.rstrip()
    x = re.findall(regex,line)
    if len(x)>0:
        #flist.append(x)
        summed+=float(x[0])
        counter+=1

print (summed/counter)
'''
Here's what's going on here:
1- Obviously, we input the path to the file that needs analysis.
2- Next, input the regex that we use on this file. Note that this regex can also be
fed directly into the loop below. But I like the aesthetics of using a variable named
regex in the loop.
3- The for loop goes through the file line by line. In each line the specified regex is
extracted and after excluding matches of len(0), is sent down for further processing.
4- the result we have here is a list with a str(number). So, we extract that item
as float, and += it in summed.
5- finally, since we are taking an average here we need a counter.
'''