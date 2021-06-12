from socket import socket, AF_INET, SOCK_STREAM

host = "localhost"
port = 6666

sock = socket(AF_INET, SOCK_STREAM)

sock.connect((host, port))
print("client connecté enft")
