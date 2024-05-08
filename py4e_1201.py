import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)
counter=0
while True:
    data=mysock.recv(1)
    #print (data)
    if len(data)<1:
        break
    counter+=1
    if counter==3000:
        break
    print (data.decode(), end="")
print (counter)
mysock.close()
