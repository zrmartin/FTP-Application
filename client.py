from socket import *
import pickle
import sys



if len(sys.argv) != 3:
	sys.exit("Format: python3 client.py <ip_address> <port_number>")

serverAddress = sys.argv[1]
serverPort = int(sys.argv[2]) 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverAddress, serverPort))

while True:
	command = input("Choose command: 'list, get <filename>, exit' ")	#Get user command
	clientSocket.send(pickle.dumps(command))
	
	if command == "exit":
		clientSocket.close()
		sys.exit("User has quit the program, goobye!")
	elif command == "list":
		f_list = pickle.loads(clientSocket.recv(1024))
		print (f_list)
	elif command.split(" ")[0] == "get":
		result = pickle.loads(clientSocket.recv(1024))
		if (result):
			file = open(command.split(" ")[1], "wb")
			while (result > 0):
				data = clientSocket.recv(1024)
				file.write(data)
				result -= len(data)
			file.close()
		else:
			print("File does not exist")
	else:
		pass