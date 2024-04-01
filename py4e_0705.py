fhand=open (input ("Please enter file path here >>> "))     #mbox.txt or mbox-short.txt
count=0
for line in fhand:
    line.rstrip()
    if line.startswith("From "):
        split_line=line.split()
        count+=1
        print (split_line[1])
print(count)