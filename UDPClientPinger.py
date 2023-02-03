import socket
from socket import *

import time
print ('Running')
serverName = 'localhost'
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
sequence_number = 1

while sequence_number<=10:

    message = ('ping').encode()
    start=time.time()
    clientSocket.sendto(message,(serverName, 8000))

    try:

        message, address = clientSocket.recvfrom(1024)
        elapsed = (time.time()-start)
        print (sequence_number)
        print (message)
        print ('Round Trip Time is:' + str(elapsed) + ' seconds')

    except timeout:
        print (sequence_number)
        print ('Request timed out')
    sequence_number+=1

if sequence_number > 10:
    clientSocket.close()
