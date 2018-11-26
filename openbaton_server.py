import socket
import time
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
HOST=''
PORT = 44444
server.bind((HOST, PORT))
dict={}
IPlist=[]
serviceName='123'
while True:
	data, addr = server.recvfrom(65536)
	try: 
		x = int(data)
		try:
			dict[serviceName].append(addr[0])
		except KeyError:
			print("VM doesn't exist.")
	except ValueError: 
		serviceName = data
		if serviceName not in dict:
			dict[serviceName]=list() 	
	for i in dict.items():
		print(i[0],i[1])
	

	
	

	

