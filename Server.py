import socket

Songname="Enter Song File Name Here"

with open(Songname, "rb") as file:      #Extracts Binary Information From MP3 File
    binary_data = file.read()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 9999))

server.listen()

client, addr = server.accept()

done = False

while not done:
    msg = client.recv(1024).decode('utf-8')
    if msg == "quit":
        done = True
    elif msg == "1":
        client.send(binary_data)




client.close()
server.close()