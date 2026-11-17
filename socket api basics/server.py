import socket
import time
# How does the server work, and how does the kernel tell the sockets apart?

# Each client gets its own accepted socket. Every one of them has local port 8000.
# The kernel keeps a lookup table keyed by the 4-tuple: (client IP, client port, server IP, server port).
# For each incoming packet, the kernel does this:
# Matches an existing connection: the packet goes to that accepted socket’s receive buffer.
# No match, and it’s a SYN to port 8000: it goes to the listening socket, which starts a new connection.
# Two clients always differ in client IP or client port. Even the same client opening two connections uses two different ephemeral ports.
# Your recv() on client_socket reads only the data that matched that socket’s 4-tuple.

# Key idea: a port is just a number in the packet header. It is not a container owned by one socket. The 4-tuple is what makes each connection unique.

# create socket obj  (it asks OS for a available socket )
s = socket.socket()   # that socket only watches for incoming TCP SYN
s.bind(("localhost",8000))      # Bind socket (binds the socket to a specified port)
s.listen()                      # socket on listening state 

# accepts incoming client connections
client_socket ,client_addr= s.accept()

# send/receive data in a infinte loop controlled by a flag
database = {"apple":5,"banana":10,"grappes":23}
flag = 1  
while True: 
    try:
        key = (client_socket.recv(64)).decode("utf-8")
        print(f"[{client_socket}] ")
        if key in database:
            msg = f"shop has {database[key]} {key} total" 
            client_socket.sendall(msg.encode("utf-8"))  
        else:
            client_socket.send(b"no such product exist in shop")
        flag+=1
    except KeyboardInterrupt :
        print("closing server !!")
        break
    
client_socket.close()
print("server closed !!!1")
    
    