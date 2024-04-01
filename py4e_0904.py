myfile=open (input ("Please enter file path here >>> "))        #mbox.txt or mbox-short.txt
mydict=dict()
for line in myfile:
    line.rstrip()
    if line.startswith("From:"):
        target_list=line.split()
        target_address = (target_list[1])
        #print (target_address)
        if target_address not in mydict:
            mydict[target_address]=1
        else:
            mydict[target_address]+=1


max_email=max(mydict,key=mydict.get)
print ("The email address with highest number of emails is ",max_email, "with ",mydict[max_email],"emails.")