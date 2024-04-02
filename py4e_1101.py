import re

file = input ("Enter the file path \n>>>")       #mbox.txt or mbox-short.txt
regex=input("Please enter a regular expression \n>>>")

fhand = open (file,'r')
counter=0
for line in fhand:
    line=line.rstrip()
    if re.search(regex,line):
        counter+=1
print ("Your file had", counter, "lines that matched", regex)