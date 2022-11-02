
import random
import math
import time

from BitVector import *
def generate_prime(k):
	while True:
		bv = BitVector(intVal=0)

		bv = bv.gen_rand_bits_for_prime(k)
		check = bv.test_for_primality()
		if (check > 0.9999):
			val = int(bv)
			return val

def key_pair_generation(sz):
    p = generate_prime(sz)
    q = generate_prime(sz)

    n = p * q

    phi_OF_n = (p - 1) * (q - 1)

    e = selectE(phi_OF_n)

    gcd, x, y = extented_euclidean_algorthm(e, phi_OF_n)

    if (x < 0):
        d = x + phi_OF_n;
    else:
        d = x
    return ((e,n),(d,n))

def GCD(x,y):
	if(y == 0):
		return x
	else:
		return GCD(y,x%y)

def selectE(phi):
	while(True):
		e = random.randrange(2,phi)
		if(GCD(e,phi) == 1):
			return e

def extented_euclidean_algorthm(a,b):
	x,old_x = 0 , 1
	y,old_y = 1 , 0
	while (b!=0):
		quotient = a // b
		a,b = b, a - quotient * b
		old_x ,x = x, old_x - quotient * x
		old_y, y = y, old_y -  quotient * y

	return  a,old_x,old_y

def encryption(public_key,msg):
    e,n=public_key
    encrypted_msg = []
    for i in msg:
        temp = ord(i)
        encrypted_msg.append(pow(temp,e,n))
    return encrypted_msg


def decryption(private_key,encrypted_msg):
    d,n=private_key
    plan_text = ''
    for i in encrypted_msg:
        temp = pow(i,d,n)
        plan_text=plan_text + str(chr(temp))
    return plan_text























