#MATH 314
#GROUP 1
#PROJECT 7
#DECEMBER 8, 2020
import socket
import threading
import config
from cryptography.fernet import Fernet

#No changes were made to the server
#We understand we will need to implement the decyrpt method here
#We were unsuccessful in decrypting the messages due to errors we could not troubleshoot

class Server:
    def __init__(self):
        self.start_server()

    def start_server(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = socket.gethostbyname(socket.gethostname())
        port = int(input('Enter port to run the server on --> '))

        self.clients = []

        self.s.bind((host, port))
        self.s.listen(100)

        print('Running on host: ' + str(host))
        print('Running on port: ' + str(port))

        self.username_lookup = {}

        while True:
            c, addr = self.s.accept()

            username = c.recv(1024).decode()

            print('New connection. Username: ' + str(username))
            self.broadcast('New person joined the room. Username: ' + username)

            self.username_lookup[c] = username

            self.clients.append(c)

            threading.Thread(target=self.handle_client, args=(c, addr,)).start()

    def broadcast(self, msg):
        for connection in self.clients:
            connection.send(msg.encode())

    def handle_client(self, c, addr):
        while True:
            try:
                msg = c.recv(1024)
                
            except:
                c.shutdown(socket.SHUT_RDWR)
                self.clients.remove(c)

                print(str(self.username_lookup[c]) + ' left the room.')
                self.broadcast(str(self.username_lookup[c]) + ' has left the room.')

                break

            if msg.decode() != '':
                #HERE IS WHERE DECRYPTION WILL OCCUR
                #val = config.f.decrypt(msg)
                print('New message: ' + str(msg.decode()))
                for connection in self.clients:
                    if connection != c:
                        connection.send(msg)


server = Server()