my_file=open (input ("Please enter file path here >>> "))       #mbox.txt or mbox-short.txt
my_dict=dict()

for line in my_file:
    line=line.rstrip()
    if line.startswith("From "):
        target_list=line.split()
        target_day=target_list[2]
        if target_day not in my_dict:
            my_dict[target_day]=1
        else:
            my_dict[target_day]+=1
print (my_dict)            

