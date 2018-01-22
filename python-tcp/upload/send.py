import sys
import socket 

TCP_IP = "127.0.0.1"
TCP_PORT = 5005
TEMP = 'upload/'
FILE_NAME = 'test-img.png'

print "TCP target IP:", TCP_IP
print "TCP target port:", TCP_PORT
print "Image:", TEMP + FILE_NAME

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))

fUploadFile = open(TEMP+FILE_NAME, "rb")
Read = fUploadFile.read(1024)
while Read:
    sock.send(Read)
    sRead = fUploadFile.read(1024)
print "Sending Completed"
