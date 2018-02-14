from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
    message = raw_input('Input lowercase sentence:')
    clientSocket.sendto(message, (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print "================"
    print "modified message: " + modifiedMessage
    print "server address"
    print serverAddress
    print "server name: " + serverName
    print "================"
