#MATH 314
#GROUP 1
#PROJECT 7
#DECEMBER 8, 2020
#This script is to allow us to call the key from both server and client since it is not a asymmtetric implementation of a key exchange.
from cryptography.fernet import Fernet
key = Fernet.generate_key() #Key is generated
f = Fernet(key) #Assign the key to a variable to be used
