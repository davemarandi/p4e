fhand = open (input ("Please enter file path here >>> "))        #mbox.txt or mbox-short.txt
mydict=dict()
for line in fhand:
    line.rstrip()
    if line.startswith("From:"):
        l=line.split()
        address=l[1]
        if address not in mydict:
            mydict[address]=1
        else:
            mydict[address]+=1
#print (mydict)
mylist=list()
for email, count in mydict.items():
    mylist.append((count,email))

#print (mylist)
mylist.sort(reverse=True)
for count, email in mylist[:1]:
    print (email, count)