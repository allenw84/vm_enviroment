import socket
import time
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
#server.settimeout(0.2)
HOST=''
PORT = 44444
server.bind((HOST, PORT))
#server.listen()
#conn, addr = s.accept() #receive TCP the connections
dict={}
IPlist=[]
serviceName=''
while True:
	data, addr = conn.recvfrom(65536)
	try: #save the ip
		x = int(data)
		dict[serviceName].append(addr)
	except ValueError: #save the service name
		serviceName += data
		if serviceName not in dict:
			dict[serviceName]=list() 
	#dict[serviceName] = IPlist
	'''
	for i in dict.items():
		print(i[0],i[1])
	'''

	
	

	
