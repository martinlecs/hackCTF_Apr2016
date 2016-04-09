import socket
SERVER = "minion05"
PORT = 9010

# set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))

# send something
s.send("Sending a message!\n\n")

# get output
data = s.recv(1024)

# print what output you got
print data

