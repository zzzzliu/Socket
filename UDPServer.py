from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print "================"
    print "message from client: " + message
    print "client address"
    print clientAddress
    print "================"

    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
