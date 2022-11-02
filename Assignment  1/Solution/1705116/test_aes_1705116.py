
import AES_1705116 as aes
import time
from BitVector import *

input_key = input("Enter key: ")
input_key = aes.key_size_configuration(input_key)
aes.set_initial_round_key(input_key)

key_scheduling_time = time.time()
aes.key_expansion()
key_scheduling_time = time.time() - key_scheduling_time


input_pt = input("Enter plaintext: ")
b = BitVector(textstring=input_pt)
aes.plaintext_configure(input_pt)

print("Plain Text (Ascii): ",input_pt)
print("Plain Text (Hex): ",b.get_bitvector_in_hex())
print()
print("Key(Ascii): ",input_key)
print("Key(Hex): ",aes.round_keys[0].get_bitvector_in_hex())

encryption_time = time.time()
enm = aes.encryption(aes.input_plaintext)
encryption_time = time.time() - encryption_time

print()
print("Cipher Text (Hex): ",enm.get_bitvector_in_hex())
print("Cipher Text (Ascii): ",enm.get_bitvector_in_ascii())



print()
decryption_time  = time.time()
dm = aes.decryption(enm)
decryption_time = time.time() - decryption_time
print("DeCipher Text (Hex): ",dm.get_bitvector_in_hex())
print("DeCipher Text (Ascii): ",dm.get_bitvector_in_ascii())

print()
print("Execution Time : ")
print("Key Scheduling Time : ",key_scheduling_time)
print("Encryption Time: ", encryption_time)
print("Decryption Time: ",decryption_time)
