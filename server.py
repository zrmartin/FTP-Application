from socket import *
import pickle
import os
import sys
from threading import Thread

class ClientThread(Thread):

	def __init__(self):
		Thread.__init__(self)

	def run(self):
		while True:
			command = pickle.loads(connectionSocket.recv(1024))
			if command == "exit":
				connectionSocket.close()
				sys.exit("User has quit the program, goobye!")
			elif command == "list":
				fileList = os.listdir(os.getcwd())
				connectionSocket.send(pickle.dumps(fileList))
			elif command.split(" ")[0] == "get":
				command = command.split(" ")
				f_list = os.listdir(os.getcwd())
				if command[1] not in f_list:
					connectionSocket.send(pickle.dumps(0))
				else:
					fileSize = os.path.getsize(command[1])
					connectionSocket.send(pickle.dumps(fileSize))
					file = open(command[1], "rb")
					bytesRead = file.read(1024)
					while (bytesRead):
						connectionSocket.send(bytesRead)
						bytesRead = file.read(1024)
					file.close()
			else:
				pass

if len(sys.argv) > 1:
	serverPort = int(sys.argv[1])
else:
	serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
while True:
	serverSocket.listen(1)
	connectionSocket, addr = serverSocket.accept()
	newThread = ClientThread()
	newThread.start()


