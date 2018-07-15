#!/usr/bin/env python
import socket

host = '10.0.42.178'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
    command = input("ENTER")
    if command == 'EXIT':
        s.send(str.encode(command))
        break
    elif command == 'EXIT':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print (reply.decode('utf-8'))

s.close()

