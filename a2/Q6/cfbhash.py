#!/usr/bin/env python3

# A flawed cryptographic hash function based on AES and CFB mode
# (c) Alwen Tiu, 2020

from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import pad
import argparse

# The key and the iv are fixed and public.
key = b'AES-HASH-1234567'
iv = b'0123456789abcdef'
input_block_size = 32
digest_size = 16


def cfbhash(data):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    l = len(data)

    if l >= (2 ** 32):
        print("Input too long")
        raise ValueError
    print(l)
    # encode length of data in 4 bytes
    lb = long_to_bytes(l, 4)
    # add length to data and apply PKCS#7 padding
    print(len(data+lb))
    data = pad(data+lb, input_block_size)
    print(len(data))
    ct = cipher.encrypt(data)
    digest = ct[-digest_size:]
    return digest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='file to compute the hash for')
    args = parser.parse_args()

    with open(args.file, "rb") as f:
        data = f.read()
    digest = cfbhash(data)
    print(digest.hex())


if __name__ == "__main__":
    main()
