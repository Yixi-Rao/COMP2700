#!/usr/bin/env python3

# CTR MAC: a flawed construction of MAC
# (c) Alwen Tiu, 2020

import sys
from Crypto.Cipher import AES
from Crypto.Util.strxor import *
from Crypto.Util.Padding import pad
import argparse

# Fixed the IV to 12 bytes, leaving 4 bytes for the counter.
# The MAC key is secret but the IV is public so it is known to the attacker.
IV = b'0123456789ab'

# rotate a block
def rotate(b, n):
    for i in range(n):
        b = b[-1:] + b[:-1]
    return b

# compute the XOR of all blocks in the input
def xorblocks(data):
    if len(data) % AES.block_size != 0:
        raise ValueError("data length must be a multiple of block size")

    bs = AES.block_size
    n = len(data) // bs
    d = data[:bs]
    data = data[bs:]

    for i in range(n-1):
        d1 = data[:bs]
        d1 = rotate(d1, (i+1) % bs)
        d = strxor(d, d1)
        data = data[bs:]
    return d


def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CTR, nonce=IV)
    # apply PKCS#7 padding prior to encryption
    ct = cipher.encrypt(pad(data, AES.block_size))
    return ct

# generate a mac for a byte string directly
def gen_mac(data, key):
    ct = encrypt(data, key)
    m = xorblocks(ct)
    return m

# generate the mac for a file
def gen_macfile(infile, key):
    with open(infile, "rb") as f:
        data = f.read()
    return gen_mac(data, key)

# verify MAC.
def verify_mac(data, key, mac):
    m = gen_mac(data, key)
    return (m == mac)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'key', type=str, help='symmetric key for MAC; must be a 16-byte HEX string')
    parser.add_argument('file', type=str, help='file to compute the MAC for')
    parser.add_argument('--verify', dest='macvalue',
                        help='verify if MACVALUE is the correct MAC for the file; must be a 16-byte HEX string')
    args = parser.parse_args()

    with open(args.file, "rb") as f:
        data = f.read()

    key = bytes.fromhex(args.key)
    if len(key) < 16:
        print('Key must be 16 bytes')
        exit(1)

    if args.macvalue is None:
        mac = gen_mac(data, key)
        print(mac.hex())
    else:
        mac = bytes.fromhex(args.macvalue)
        if len(mac) < 16:
            print('MAC must be 16 bytes')
            exit(1)
        if verify_mac(data, key, mac):
            print('MAC is correct')
        else:
            print('MAC is incorrect')


if __name__ == "__main__":
    main()
