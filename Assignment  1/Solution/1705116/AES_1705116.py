
from BitVector import *
import time

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]


round_keys = []

AES_modulus = BitVector(bitstring="100011011")

input_plaintext = BitVector(size=0)

key_scheduling_time = 0
encryption_time = 0
decryption_time = 0

extra_pad_count =0


def plaintext_configure(plaintext):

    global input_plaintext
    new_text = size_configuration(plaintext)
    input_plaintext += BitVector(textstring=new_text)


def subsByte(bitv):

    sub_bitv = BitVector(size=0)
    len_bitv = bitv.length()

    for i in range(0,len_bitv,8):
        val = bitv[i: i+8].intValue()
        sub_bitv += BitVector(intVal=Sbox[val],size=8)
    return sub_bitv

def inverse_subsByte(bitv):
    sub_bitv = BitVector(size=0)
    len_bitv = bitv.length()

    for i in range(0,len_bitv,8):
        val = bitv[i: i+8].intValue()
        sub_bitv += BitVector(intVal=InvSbox[val],size=8)
    return sub_bitv


def size_configuration(pt):
    global extra_pad_count
    if (len(pt) > 16) :
        pt = pt[0:16]
    elif (len(pt) < 16):

        extra_pad_count = 16 - len(pt)
        pt = pt + '0' * (16 - len(pt))
    return pt

def key_size_configuration(key):
    if (len(key) > 16) :
        key = key[0:16]
    elif (len(key) < 16):
        key = key + '0' * (16 - len(key))
    return key


def set_initial_round_key(initial_key):
    initial_key_after_padding = size_configuration(initial_key)
    round_keys.append(BitVector(textstring=initial_key_after_padding))



def funtion_g(r_word,round_constant):

    r_word = r_word << 8

    r_word = subsByte(r_word)

    r_word = r_word ^ round_constant

    return r_word

def key_expansion():

    rc = BitVector(hexstring="01")
    factor = BitVector(hexstring="02")
    for i in range(10):
        round_constant = BitVector(hexstring=rc.get_bitvector_in_hex())
        round_constant += BitVector(hexstring="000000")

        w0 = round_keys[i][0:32] ^ funtion_g(round_keys[i][96:128],round_constant)
        w1 = w0 ^ round_keys[i][32:64]
        w2 = w1 ^ round_keys[i][64:96]
        w3 = w2 ^ round_keys[i][96:128]

        new_round_key = w0
        new_round_key += w1
        new_round_key += w2
        new_round_key += w3
        round_keys.append(new_round_key)

        rc = factor.gf_multiply_modular(rc, AES_modulus, 8)

def bitvector_To_matrix(bitvector):

    state_matrix = []
    for i in range(4):
        each_row = []
        bitv_length = bitvector.length()

        for j in range(bitv_length // (8 * 4)):
            start_index = (i * 8 + j * 32)
            end_index = start_index + 8

            each_row.append(bitvector[start_index:end_index])

        state_matrix.append(each_row)

    return state_matrix

def matrix_To_bitvector(state_matrix):
    converting_bitvector = BitVector(size = 0)
    col=len(state_matrix[0])
    row=len(state_matrix)

    for i in range(col):
        for j in range(row):
            converting_bitvector += state_matrix[j][i]

    return converting_bitvector

def shift_row(bitv):
    state_matrix = bitvector_To_matrix(bitv)
    for row in range(4):
        first_part = state_matrix[row][row:]
        second_part = state_matrix[row][:row]
        state_matrix[row] = first_part + second_part

    bitv_after_shift = matrix_To_bitvector(state_matrix)

    return bitv_after_shift

def inverse_shift_row(bitv):
    state_matrix = bitvector_To_matrix(bitv)
    for row in range(4):

        len_row = len(state_matrix[row])
        index = len_row - row
        first_part = state_matrix[row][index:]
        second_part = state_matrix[row][:index]

        state_matrix[row] = first_part + second_part

    bitv_after_shift = matrix_To_bitvector(state_matrix)

    return  bitv_after_shift


def matrix_mul(m1,m2):
    r_matrix = []
    row_len = len(m1)
    col_length = len(m2[0])

    for i in range(row_len):
        new_matrix_each_row = []

        for j in range(col_length):
            t = m1[i][0].gf_multiply_modular(m2[0][j],AES_modulus,8)
            t ^= m1[i][1].gf_multiply_modular(m2[1][j],AES_modulus,8)
            t ^= m1[i][2].gf_multiply_modular(m2[2][j], AES_modulus, 8)
            t ^= m1[i][3].gf_multiply_modular(m2[3][j], AES_modulus, 8)

            new_matrix_each_row.append(t)

        r_matrix.append(new_matrix_each_row)

    return r_matrix


def mix_column(bitv):
    current_state_matrix = bitvector_To_matrix(bitv)
    new_state_matrix = matrix_mul(Mixer,current_state_matrix)
    new_bitv = matrix_To_bitvector(new_state_matrix)
    return new_bitv

def inverse_mix_column(bitv):
    current_state_matrix = bitvector_To_matrix(bitv)
    new_state_matrix = matrix_mul(InvMixer, current_state_matrix)
    new_bitv = matrix_To_bitvector(new_state_matrix)
    return new_bitv

def add_round_key(bitv,round_no):
    new_bitv = bitv ^ round_keys[round_no]
    return new_bitv

def encryption(bitv):
    bitv = add_round_key(bitv,0)

    for i in range(9):
        round_no = i+1
        bitv = subsByte(bitv)
        bitv = shift_row(bitv)
        bitv = mix_column(bitv)
        bitv = add_round_key(bitv,round_no)

    round_no = 10
    bitv = subsByte(bitv)
    bitv = shift_row(bitv)
    bitv = add_round_key(bitv, round_no)

    return bitv

def decryption(bitv):
    bitv = add_round_key(bitv,10)

    for i in range(9):
        round_no =9 - i
        bitv = inverse_shift_row(bitv)
        bitv = inverse_subsByte(bitv)
        bitv = add_round_key(bitv, round_no)
        bitv = inverse_mix_column(bitv)


    round_no = 0
    bitv = inverse_shift_row(bitv)
    bitv = inverse_subsByte(bitv)
    bitv = add_round_key(bitv, round_no)
    #upto = 16 - extra_pad_count
    #idx = upto * 8
    #bitv=bitv[:idx]
    return bitv



def plaintext_configure_24(plaintext):

    global input_plaintext
    new_text = size_configuration(plaintext)
    input_plaintext += BitVector(textstring=new_text)

def size_configuration_24(initial_key):
    if (len(initial_key) > 24) :
        initial_key = initial_key[0:24]
    elif (len(initial_key) < 24):
        initial_key = initial_key + '0' * (24 - len(initial_key))
    return initial_key

def size_configuration_32(initial_key):
    if (len(initial_key) > 32) :
        initial_key = initial_key[0:32]
    elif (len(initial_key) < 32):
        initial_key = initial_key + '0' * (32 - len(initial_key))
    return initial_key




def AES_Operation(input_key,input_pt):
    set_initial_round_key(input_key)
    key_expansion()
    plaintext_configure(input_pt)
    Ci = encryption(input_plaintext)
    return Ci

def All_Value_print():
    print(round_keys)
    print(AES_modulus)
    print(input_plaintext)
    print(key_scheduling_time)
    print(encryption_time)
    print(decryption_time)
    print(extra_pad_count)
    print(encryption_time)
    print(decryption_time)
    print(extra_pad_count)

    for i in range(len(round_keys)):
        print("R:",i," : ",round_keys[i])
    print()


def round_keys_check():
    for i in range(len(round_keys)):
        print("R:",i," : ",round_keys[i])
    print()

def input_plain_text_check():
    print(input_plaintext)

def get_input_plain_text():
    return  input_plaintext

def print_encrytion_time():
    print(encryption_time)

def print_decrytion_time():
    print(decryption_time)

def scheduling_time_print():
    print(key_scheduling_time)

def en_de_time():
    print(encryption_time)
    print(decryption_time)

def extra_pad_count():

    print(extra_pad_count)

