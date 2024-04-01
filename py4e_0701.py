fhand=open (input ("Please enter file path here >>> "))  #mbox-short.txt or mbox.txt
#counter for total number of values:
counter=0
#counter for sum of all values:
countersum=0
#for loop to extract the string we need, convert to float, sum, count number of items
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue    
    lx=line.lstrip("X-DSPAM-Confidence: ")
    #print(lx)
    counter+=1
    countersum+=float(lx)
print (counter)
print (countersum)
#final result is average of these values:
final_result=countersum/counter
print (final_result)
