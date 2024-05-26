import json
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print (info)
print ('User count: ',len(info))

for i in info:
    print ("Name: ",i['name'])
    print ("Id: ",i ['id'] )
    print ("Attribute: ", i['x'])