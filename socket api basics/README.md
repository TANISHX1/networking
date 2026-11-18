
## required knowledge 
- During send / receive data always remember : 
    - str is text (Unicode), while bytes is raw 0-255 values. The network only carries bytes.
    - Encode before sending and decode after receiving.
    - TCP connect flow: SYN, then SYN-ACK if a listener exists, or RST if not.
    - Socket states: a server must go bind, then listen, then accept before a client can connect.
    - Start the server first, then the client.
- one port can have more than one socket (but 2 socket can't bind() at same port ).
- one socket can't use multiple ports

### server clinet connection 
#### server
server is a program which listens for incoming connection requests (SYN packets handle by kernel , server application nerver sees it ) . 

- it follows a sequence before listening :
  - first, it  creates a socket (internally ,asks the os for a avaliable socket )
  - ,then binds to a specific port. 
  - then it goes to listening state . and accepts the incoming connection requests
 - also , server only listen in binded port and cannot send receive data on listening port . 
- for every connection (or client ) it creates a separate socket for server clinet communication  ( sending / receving data )  .
- then ,`go back and accepts `another queued  connections (connections which has completed the handshake in kernel )  
- at a time only one  socket can be binded to a given IP:port (exception SO_REUSEPORT) , 
- multiple sockets (that are accepted ) can use the same local port without binding . 
- client sends data on the server port . the kernel de-multiplexer use 4 tuples to identifies that the incoming request is a new connection request or the connection socket already exists

#### clinet
client is a program which initiates the connection request . it also follows a procedure before send a request :

- it creates a socket (internally , it asks the os for a socket is available , ) 
- performs a DNS lookup (first the host file of the system , configured DNS resolver ) through c library , this step only happens if domin or hostname is used instead of ip .
- connect    
  - bind to a ephemeral port (client dont binds , kernel does it internally ) 
  -  performs a TCP 3 way handshake (SYN -> SYN-ACK -> ACK ) ), 
- after that it starts data send receive . 
- and at last connection close (client sends FIN Packet , if client is closing  )

we cannot directly use the network devices or kernel modules for communication because the applications runs on user space . so systems like unix /linux and C provides a system -call interface or api called Socket (also a socket is a file descriptor in unix like sys ) to communicate with kernel network stack for communication. and the kernel network stack talks to the network devices .
operations like send , recv , are blocking operations by default

### Output
![Alt Text](image.png)

### Remember

- Socket: a kernel-managed endpoint (fd) identified by protocol + local IP:port (+ remote IP:port once connected).

- What does accept() in python return? A new connected socket plus the client’s address.

- How does the server serve many clients on one port? The kernel demultiplexes by 4-tuple.

- Why is recv() not message-based? TCP is a byte-stream protocol . and it can be message-based if UDP protocol is used  

- What is TIME_WAIT? The state kept by the active closer, which lets old packets expire and makes sure the final ACK arrives.

- bind() vs listen() vs accept(): assign an address; mark the socket passive and start the backlog; take one completed connection.

- Packet vs circuit switching: shared links and independent packets, vs a reserved dedicated path.