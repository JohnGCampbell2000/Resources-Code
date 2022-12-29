# Import socket module
from socket import *    

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Finish creating server socket

# Place code here (10 points)
serverPort = 6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
	print('Ready to serve...')
	
	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()# Place code here (5 points)
	
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		message = connectionSocket.recv(1024) # Place code here (5 points)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		# Store the entire content of the requested file in a temporary buffer
		outputdata = f.read()# place code here (5 points)
		# Send the HTTP response header line to the connection socket

                # Place code here (10 points)
		connectionSocket.send('\n'.encode())
		connectionSocket.send('HTTP/1.1 200 OK\n'.encode())
		connectionSocket.send('Connection: close\n'.encode())
		connectionSocket.send('Content-Type: text/html\n'.encode())
		connectionSocket.send('\n'.encode())
		connectionSocket.send('\n'.encode())
		connectionSocket.send('<h1>Hello World! ;)</h1>'.encode())

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(bytes(outputdata[i],"utf-8"))
		connectionSocket.send(bytes("\r\n","utf-8"))
		
		# Close the client connection socket
		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found

                # Fill in code here (10 points)
		connectionSocket.send('\n'.encode())
		Message404 = ('HTTP/1.1 404 not found\n'.encode())
		connectionSocket.send(Message404)

		# Close the client connection socket

# Fill in code here (5 points)
connectionSocket.close()
serverSocket.close()  

