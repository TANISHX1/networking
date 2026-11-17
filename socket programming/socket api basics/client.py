import socket

#  create a socket object
s = socket.socket()
# connect to host (it also do DNS lookup internally)
s.connect(("127.0.0.1",8000))
print(s)
print("*"*70)
# s.sendall(b"send all data at once")
while True:
    try:
        inp = input("Enter the item name to check:\t")
        s.send(inp.encode("utf-8"))  # might do partial send
        data = s.recv(256)  #receive at most 256 bytes of data at most 
        print(data.decode("ASCII"))
        
    except EOFError: 
        print("Exiting !!")
        break