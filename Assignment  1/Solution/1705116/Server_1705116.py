
import socket
import AES_1705116 as aes
import RSA_1705116 as rsa
import os
from BitVector import  *

parent_dir = "E:/"
directory = "Don't_Open_this"
DPT_file_path = "E:\Don't_Open_this\DPT.txt"
PRK_file_path = "E:\Don't_Open_this\PRK.txt"


def file_write_operation(PRK):

    path = os.path.join(parent_dir, directory)

    os.mkdir(path)

    file1 = open(PRK_file_path, "w")

    str1 = str(PRK[0])
    str2 = str(PRK[1])

    file1.write(str1)
    file1.write("\n")
    file1.write(str2)
    #file1.write("\n")
    file1.close()

def DPT_file_read():
    file1 = open(DPT_file_path, "r")
    str3 = file1.readline()
    return str3

def connection_estabilishment():
    s = socket.socket()
    print("Socket successfully created")
    port = 12345
    s.bind(('', port))
    print("socket binded to %s" % (port))
    s.listen(5)
    print("socket is listening")
    while True:
        global c
        c, addr = s.accept()
        print('Got connection from', addr)
        break


def AES_Operation(input_key,input_pt):
    aes.set_initial_round_key(input_key)
    aes.key_expansion()
    aes.plaintext_configure(input_pt)
    CT = aes.encryption(aes.input_plaintext)
    return CT
def RSA_Operation(keyLength,plaintext):
    primeNumberSize = int(keyLength / 2)
    public_key, private_key = rsa.key_pair_generation(primeNumberSize)
    EK = rsa.encryption(public_key, plantext)

    return public_key,private_key,EK

def sendToClient(msg):
    c.send(msg.encode())

def send_EK(EK):
    EK = str(EK)
    EK = EK.encode()
    c.send(EK)
def send_CT( CT ):
    ascii_CT = CT.get_bitvector_in_ascii()
    #new_CT = str(ascii_CT)
    new_CT = ascii_CT.encode()
    c.send(new_CT)

def send_PUK(PUK):
    PUK = str(PUK)
    PUK = PUK.encode()
    c.send(PUK)

def receiveFromClient():

    msg = c.recv(1024).decode()
    return msg



connection_estabilishment()

input_key = input("Enter key: ")

input_key = aes.key_size_configuration(input_key)
print("Key after padding: ",input_key)
input_pt = input("Enter plaintext: ")



CT = AES_Operation(input_key,input_pt)

print("Original Plain Text after padding: ",aes.input_plaintext.get_text_from_bitvector())
keyLength = int(input("Enter key length : "))
plantext = input_key

PUK,PRK,EK = RSA_Operation(keyLength,plantext)

print()
print("CT: ",CT.get_bitvector_in_ascii())
print("EK: ",EK)
print("PUK: ",PUK)
print("PRK: ",PRK)

file_write_operation(PRK)

PUK_list = [1,2]
PUK_list[0] = PUK[0]
PUK_list[1] = PUK[1]

send_CT(CT)
send_EK(EK)
#send_PUK(PUK_list)

is_complete_dpt = receiveFromClient()

if is_complete_dpt == "yes":

    DPT = DPT_file_read()
else:
    DPT = ""
#b1=BitVector(textstring =input_pt)
#b2 = BitVector(textstring=DPT)
#b3 = b1 ^ b2
print()
print("Original plaintext: ",aes.input_plaintext.get_text_from_bitvector())
print("DPT: ",DPT)
print()
DPT = BitVector(textstring=DPT)
if aes.input_plaintext == DPT :
    print("DPT and Original plaintext matched")
else:
    print("DPT and Original plaintext - Not matched")

c.close()

