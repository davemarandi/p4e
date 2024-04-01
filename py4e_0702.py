romeo=open (input ("Please enter file path here >>> "))             #py4e_files/romeo.txt
romeo_list=list()
for line in romeo:
    poem_line=line.split()
    for word in poem_line:
        if word not in romeo_list:
            romeo_list.append(word)
romeo_list.sort()

print(romeo_list)