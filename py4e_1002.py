# This program counts the distribution of the hour of the day for
# each of the emails in a file

myfile=open (input ("Please enter file path here >>> "))        #mbox.txt or mbox-short.txt
mydict=dict()
mylist=list()
for line in myfile:
    line.rstrip()                                   # for loop to read each line of file
    if line.startswith("From "):
        l=line.split()                              # find lines starting with "from" and split that line into a list
        #print (line)
        num=(l[5])                                  # we have business with the 5th item in this list in each iteration
        #print (num[:2])
        the_number=(num[:2])                        # from 5th item which is a bunch of numbers (time+date) we extract the hour
        if the_number not in mydict:
            mydict[the_number]=1                    # if hour is not in dictionary add it as a key and count 1 otherwise +=1
        else:
            mydict[the_number]+=1
#print (mydict)
for time, count in mydict.items():
    mylist.append((time,count))
mylist.sort()

for count, time in mylist[:]:
    print (count, time)