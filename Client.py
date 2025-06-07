import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerIP = "Enter Server IP Address Here"

sock.connect((ServerIP, 9999))

done = False
print("1: Animals Maroon 5")
n=input("Message: ")
sock.send(n.encode('utf-8'))

msg = sock.recv(100000000)


with open("clientrequest.mp3", "wb") as f:
    f.write(msg)

