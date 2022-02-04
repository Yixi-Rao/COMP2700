#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import *
from Crypto.Util.strxor import *
import argparse


def bbc_encrypt(iv, key, data):

    pt = pad(data, AES.block_size)

    cipher = AES.new(key, AES.MODE_ECB)
    e = cipher.encrypt(pt)
    bs = AES.block_size

    k = len(pt) // bs
    ct = bytes(0)
    y = iv
    for i in range(k):
        y = strxor(e[i * bs : (i + 1) * bs], y)
        ct = ct + y
    print(len(ct))
    return ct


def bbc_decrypt(iv, key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    bs = AES.block_size

    k = len(data)//AES.block_size
    e = bytes(0)
    x = iv
    for i in range(k):
        y = data[i*bs:(i+1)*bs]
        x = strxor(x, y)
        e = e + x
        x = y
    pt = cipher.decrypt(e)

    pt = unpad(pt, bs)
    return pt


def test():
    key = b'0123456789abcdef'
    iv = b'0101010101010101'
    with open('Q4/plain1.txt', 'rb') as f:
        pt = f.read()
    ct = bbc_encrypt(iv, key, pt)
    
    with open('Q4/try.enc', 'wb') as f:
        f.write(ct)
    flag = b'0123456789abcde-flag{mad-helm}  '
    flag = bbc_encrypt(iv, key, flag)
    with open('Q4/flag.enc', 'wb') as f:
        f.write(flag)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'key', type=str, help='encryption key; must be a 16-byte HEX string')
    parser.add_argument(
        'iv', type=str, help='IV; must be a 16-byte HEX string')
    parser.add_argument('infile', type=str,
                        help='input file to encrypt/decrypt')
    parser.add_argument('outfile', type=str,
                        help='output file containing the result')
    parser.add_argument('--decrypt', default=False,
                        action='store_true', help='decrypt rather than encrypt')
    args = parser.parse_args()

    with open(args.infile, "rb") as f:
        data = f.read()

    key = bytes.fromhex(args.key)
    if len(key) < 16:
        print('Key must be 16 bytes')
        exit(1)
    iv = bytes.fromhex(args.iv)
    if len(iv) < 16:
        print('IV must be 16 bytes')
        exit(1)

    if args.decrypt:
        print('Decrypting file')
        pt = bbc_decrypt(iv, key, data)
        with open(args.outfile, 'wb') as f:
            f.write(pt)
    else:
        print('Encrypting file')
        ct = bbc_encrypt(iv, key, data)
        with open(args.outfile, 'wb') as f:
            f.write(ct)


if __name__ == "__main__":
    test()
