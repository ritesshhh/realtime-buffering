import socket
import time


HEADERSIZE = 10
PREV_LINE_NO = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1243))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg

    clientsocket.send(bytes(msg,"utf-8"))
    '''
    while True:
        f = open('example.txt', 'r')
        file_contents = f.read(1)
        print (file_contents)
        msg = file_contents
        	
        time.sleep(1)
        #msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg
        
        print(msg)

        clientsocket.send(bytes(msg,"utf-8"))
     '''

    while True:
        f = open('example.txt', 'r')
        for i, line in enumerate(f):
            if i > PREV_LINE_NO:
               msg = line
        	
               time.sleep(1)
               msg = f"{len(msg):<{HEADERSIZE}}"+msg
               print(msg)

               clientsocket.send(bytes(msg,"utf-8"))
               PREV_LINE_NO = i
