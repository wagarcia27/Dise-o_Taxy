from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'57487',('localhost', 37777))
print(s.recvfrom(8192))



