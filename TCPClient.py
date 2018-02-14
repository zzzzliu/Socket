from socket import *
serverName = 'localhost'
serverPort = 12000

while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort)) # every time you create a new connection, you need to handshake again
    sentence = raw_input("Input lowercase sentence: ")
    clientSocket.send(sentence)
    modifiedSentence = clientSocket.recv(1024)
    print 'From Server: ', modifiedSentence
    print "server name: " + serverName
    print "================"
    clientSocket.close()
