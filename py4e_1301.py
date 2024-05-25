import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("URL ")
response=urllib.request.urlopen(url, context=ctx)
data=response.read()
tree=ET.fromstring(data)

lst=tree.findall('comments/comment')
total=len(lst)
print('Total =',total)

count=list()
for item in lst:
    a=int(item.find('count').text)
    count.append (a)


print ("Sum = ",sum(count))