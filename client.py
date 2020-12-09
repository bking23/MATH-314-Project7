#MATH 314
#GROUP 1
#PROJECT 7
#DECEMBER 8, 2020
import socket
import threading
import config
from cryptography.fernet import Fernet

class Client:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while 1:
            try:
                host = input('Enter host name --> ')
                port = int(input('Enter port --> '))
                self.s.connect((host, port))

                break
            except:
                print("Couldn't connect to server")

        self.username = input('Enter username --> ')
        self.s.send(self.username.encode())

        message_handler = threading.Thread(target=self.handle_messages, args=())
        message_handler.start()

        input_handler = threading.Thread(target=self.input_handler, args=())
        input_handler.start()



    def handle_messages(self):
        while 1:
            inc_msg = self.s.recv(1204).decode()
            #This is where decryption will occur
            #We were unsuccessful in decrypting the messages
            #Below is what we believe should work but currently does not
            #dec = bytes(inc_msg, 'utf-8')
            #print(config.f.decrypt(inc_msg))
            print(inc_msg)

    def input_handler(self):
        while 1:
            msg = input()#take user input
            bytes_msg = bytes(msg, 'utf-8')#convert string to bytes
            token = config.f.encrypt(bytes_msg) #encrypt the data
            token1 = str(token)#convert back to string
            self.s.send((self.username + ' - ' + token1).encode()) #send the data to the server


client = Client()
