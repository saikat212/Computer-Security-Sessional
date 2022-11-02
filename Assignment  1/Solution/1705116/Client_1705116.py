import socket
import AES_1705116 as aes
import RSA_1705116 as rsa
import os
from BitVector import *
parent_dir = "E:/"
directory = "Don't_Open_this"
DPT_file_path = "E:\Don't_Open_this\DPT.txt"
PRK_file_path = "E:\Don't_Open_this\PRK.txt"


def file_write_operation(DPT):
    #file1 = open(r"E:\pythonProject\Don't_Open_this\DPT.txt", "w+")
    file1 = open(DPT_file_path, "w")
    file1.write(DPT)
    #file1.write("\n")
    file1.close()


def connection_estabilish():
    global s
    s = socket.socket()
    port = 12345
    s.connect(('127.0.0.1', port))

def key_decryption_using_rsa(PRK,EK):
    plaintext = rsa.decryption(PRK,EK)
    return plaintext

def AES_Decryption_Operation(AES_key,CT):

    aes.set_initial_round_key(AES_key)
    aes.key_expansion()
    DPT = aes.decryption(CT)
    return DPT


def PRK_file_read():
    file1 = open(PRK_file_path, "r")
    str3 = file1.readline()
    str4 = file1.readline()
    val_d = int(str3)
    val_n = int(str4)
    PRK = (val_d, val_n)
    return PRK

def recv_EK():
    data = s.recv(4096)
    data = data.decode('utf-8')
    data = eval(data)
    return data

def recv_PUK():
    data = s.recv(4096)
    data = data.decode('utf-8')
    data = eval(data)
    return data

def recv_CT():
    data = s.recv(1024)
    data = data.decode()
    return data

def receiveFromServer():

    msg = s.recv(1024).decode()
    return msg
def sendToServer(msg):
    s.send(msg.encode())

connection_estabilish()

CT = recv_CT()
EK = recv_EK()
#PUK = recv_PUK()


PRK = PRK_file_read()
AES_key = key_decryption_using_rsa(PRK,EK)
print()
print("CT: ",CT)
print("EK: ",EK)
print("PRK: ",PRK)
#print("PUK: ",PUK)

CT = BitVector(textstring=CT)
DPT = AES_Decryption_Operation(AES_key,CT)
DPT = DPT.get_bitvector_in_ascii()

file_write_operation(DPT)
sendToServer("yes")

print("DPT:",DPT)

s.close()




