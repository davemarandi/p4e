import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inp=input("please enter url \n")
try:
    inp1=inp.split('/')
    inp3=inp1[2]
    #print (inp)
    #mysock.connect(('data.pr4e.org', 80))
    mysock.connect((str(inp3), 80))
    alpha=('GET '+str(inp)+ ' HTTP/1.0\r\n\r\n').encode()
    #cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    cmd = alpha
    print(str(inp3), cmd)
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print ("invalid, f off")