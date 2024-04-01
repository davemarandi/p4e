myfile=open (input ("Please enter file path here >>> "))        #words.txt
mydict=dict()
for line in myfile:
    file_line=line.split()
    print (line)
    for word in file_line:
        if word not in mydict:
            mydict[word]=1
        else:
            mydict[word]+=1

print (mydict)