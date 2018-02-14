from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
    connectionSocket, clientAddress = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    print "=============="
    print "the server socket for handshaking: "
    print serverSocket
    print "sentence from client: " + sentence
    print "client address: "
    print clientAddress
    print "temporal connection Socket: "
    print connectionSocket
    print "=============="
    connectionSocket.close()
