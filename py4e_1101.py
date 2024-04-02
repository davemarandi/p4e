import re
file = input ("Enter the file path \n>>>")       #mbox.txt or mbox-short.txt
regex=input("Please enter a regular expression \n>>>")
fhand = open (file,'r')

#regular=str(inp)
counter=0
print (regex)
for line in fhand:
    line=line.rstrip()
    for line in fhand:
        if re.search(regex,line):
        #if len(x)>0:
            counter+=1
print ("Your file had", counter, "lines that matched", regex)