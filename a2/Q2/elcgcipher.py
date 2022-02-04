#!/usr/bin/env python3

# ANU COMP2700 Cyber Security Foundations
# A simple (and flawed) stream cipher using a linear congruence generator
# Alwen Tiu, 2021


import sys
from Crypto.Util.number import *
from Crypto.Util.strxor import *

# Each block is 2 bytes
BLOCK_SIZE = 2
# Fixed the modulus; must be representable as a 2-byte integer.
MODULUS = 64283


# All key material S0, A, B and p are 16-bit integers (2 bytes)
def elcg(S0, S1, A, B, C, n):
    Sa = S0
    Sb = S1
    keystream = bytearray()

    # generate a 2-byte pseudo-random number at a time.
    for i in range(n):
        Sc = (A * Sb + B * Sa + C) % MODULUS
        R = bytearray(long_to_bytes(Sc, BLOCK_SIZE))
        if i < 5:
            print(bytes_to_long(R))
        keystream.extend(R)
        Sa = Sb
        Sb = Sc
    return bytes(keystream)

# NOTE: since this is a streamcipher, encryption and decryption are the same function.


def encrypt(S0, S1, A, B, C, inbytes):
    sz = len(inbytes)

    # generate keystream
    # n = how many random numbers need to be generated.
    # Each number is BLOCK_SIZE byte long.
    n = sz // BLOCK_SIZE + 1
    keystream = elcg(S0, S1, A, B, C, n)

    # byte-wise XOR plaintext with keystream
    outbytes = strxor(inbytes, keystream[0:sz])
    return outbytes

# NOTE: since this is a streamcipher, encryption and decryption are the same function.


def encfile(S0, S1, A, B, C, infile, outfile):
    with open(infile, 'rb') as f:
        inbytes = f.read()
    outbytes = encrypt(S0, S1, A, B, C, inbytes)

    with open(outfile, 'wb') as g:
        g.write(outbytes)


def main():
    # if len(sys.argv) < 8:
    #     print("Usage: python3 " + sys.argv[0] + " S0 S1 A B C infile outfile ")
    #     quit()
    # S0 = int(sys.argv[1]) % MODULUS
    # S1 = int(sys.argv[2]) % MODULUS
    # A = int(sys.argv[3]) % MODULUS
    # B = int(sys.argv[4]) % MODULUS
    # C = int(sys.argv[5]) % MODULUS
    # encfile(S0, S1, A, B, C, sys.argv[6], sys.argv[7])
    encfile(25426, 12948, 38061, 2483, 15677, "Q2/try.txt", "Q2/tryenc.enc" )

if __name__ == "__main__":
    main()
