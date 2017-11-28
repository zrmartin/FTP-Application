This is a simple FTP application.
The client may view and download any files in the directory where the server.py file is located

In order to run the program, run the following commands:
python3 server.py <port_number> if no port_number is given it defaults to 5000
python3 client.py <ip_address> <port_number>

Once the client and server are running, the client may enter the following commands:
list: to list all of the files available for download in the server's current directory
get <filename>: to download the given file from the server
exit: to quit the program
