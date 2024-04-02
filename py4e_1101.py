file = open ("/mbox.txt")       #mbox.txt or mbox-short.txt
import re
inp=input("Please enter a regular expression \n>>>")
regular=str(inp)
counter=0
print (regular)
for line in file:
    line=line.rstrip()
    for line in file:
        x=re.findall(regular, line)
        if len(x)>0:
            counter+=1
print ("Your file had", counter, "lines that matched", inp)