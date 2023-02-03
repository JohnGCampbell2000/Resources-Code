# Import socket module
from socket import *    

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
	print('Ready to serve...')
	
	connectionSocket, addr = serverSocket.accept()
	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()

		connectionSocket.send('\n'.encode())
		connectionSocket.send('HTTP/1.1 200 OK\n'.encode())
		connectionSocket.send('Connection: close\n'.encode())
		connectionSocket.send('Content-Type: text/html\n'.encode())
		connectionSocket.send('\n'.encode())
		connectionSocket.send('\n'.encode())
		connectionSocket.send('<h1>Hello World! ;)</h1>'.encode())

		for i in range(0, len(outputdata)):  
			connectionSocket.send(bytes(outputdata[i],"utf-8"))
		connectionSocket.send(bytes("\r\n","utf-8"))
		
		connectionSocket.close()

	except IOError:

		connectionSocket.send('\n'.encode())
		Message404 = ('HTTP/1.1 404 not found\n'.encode())
		connectionSocket.send(Message404)

connectionSocket.close()
serverSocket.close()  

