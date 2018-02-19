# Socket
Python Socket demo with UDP and TCP protocol

## UDP Protocol
In this application, we use UDP Protocol for the application-layer
Socket. The client send a message to server, and server change
all letters to uppercase, and then send back to client. Please note that
in UDP protocol, we don't have to confirm connection (handshaking).

First run `UDPServer.py` to start the server.

```
python UDPServer.py
```
Then run client-side
application `UDPClient.py`.
```
python UDPClient.py
```

* UDPServer.py

    The server port is 12000, and the address is localhost.

* UDPClient.py

    The program doesn't specify the port and IP address for client side.
    Instead, the operating system do that for us automatically.

## TCP Protocol

In this application, we use TCP Protocol for the application-layer
Socket. The client send a message to server, and server change
all letters to uppercase, and then send back to client. Please note that
in TCP protocol, we have to confirm connection first then start
sending data.

First run `TCPServer.py` to start the server.

```
python TCPServer.py
```
Then run client-side
application `TCPClient.py`.
```
python TCPClient.py
```


* TCPServer.py

    The server port is 12000, and the address is localhost.
    First initiate the socket and specify the waiting queue size.

    ```
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.listen(1)
    ```

    In each communication, `serverSocket.accept()` confirm the connection
    and getting back the address of client, as well as a connection
    socket `connectionSocket`. So in each TCP connection, we have two
    socket - `serverSocket` for handshaking and `connectionSocket` for
    sending data.

* TCPClient.py
    The program doesn't specify the port and IP address for client side.
    Instead, the operating system do that for us automatically. Basically,
    the IP address is 127.0.0.1, which means in this application, the
    client and server are on a same host - localhost.