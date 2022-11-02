
import RSA_1705116 as rsa
import time

if __name__ == '__main__':
    keyLength = int(input("Enter key length : "))
    primeNumberSize = int(keyLength / 2)
    key_generation_time =0
    encryption_time =0
    decryption_time =0


    key_generation_time = time.time()
    public_key,private_key=rsa.key_pair_generation(primeNumberSize)
    key_generation_time = time.time() -key_generation_time

    print("Public Key: ",public_key)
    print("Private Key:",private_key)

    plantext = input("Enter plaintext: ")

    encryption_time = time.time()
    cipher_text=rsa.encryption(public_key,plantext)
    encryption_time = time.time() - encryption_time
    print("Cipher Text :\n ",cipher_text)

    decryption_time = time.time()
    decrypted_text = rsa.decryption(private_key,cipher_text)
    decryption_time = time.time() - decryption_time
    print("Decrypted Text: \n",decrypted_text)

    print()
    print("Execution Time : ")
    print("Key Generation Time : ",key_generation_time)
    print("Encryption Time : ",encryption_time)
    print("Decryption Time : ",decryption_time)