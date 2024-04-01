myfile=open (input ("Please enter file path here >>> "))        #mbox.txt or mbox-short.txt
mydict=dict()
for line in myfile:
    line.rstrip()
    if line.startswith("From:"):
        target_list=line.split()
        target_address = (target_list[1])
        target_address_split=target_address.split('@')
        domain=target_address_split[1]
        #print (domain)
        if domain not in mydict:
            mydict[domain]=1
        else:
            mydict[domain]+=1
print (mydict)