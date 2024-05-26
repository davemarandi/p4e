import urllib.request, urllib.parse, urllib.error
import json
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ("URL: ")

response=urllib.request.urlopen(url, context=ctx)
data=response.read()
info=json.loads(data)

#print (info)
#print ("Count= ", len(info))
mylist=list()
for i in info:
    mylist.append(info['comments'])

mylist2=mylist[1]

mylist3=list()
for i in mylist2:
    mylist3.append (i['count'])
print ("Count =", len(mylist3))
print ("Sum =",sum(mylist3))
