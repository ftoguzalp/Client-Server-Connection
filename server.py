import socket

host="127.0.0.1"

port=50001

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((host,port))

server_socket.listen()

connection,address= server_socket.accept()

print("The adress that server is connected to is:" +str(address))

while True:
    data=connection.recv(1024).decode()
    print(data)
    response_data="Message Received    "
    connection.send(response_data.encode())
connection.close()
