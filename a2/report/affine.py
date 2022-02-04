#!/usr/bin/env python3 

# An extended affine cipher
# (c) Alwen Tiu, 2020


import sys
from Crypto.Util.number import *

def getmap(str):
    d = dict()
    for i in range(len(str)):
        d[str[i]] = i
    return d

# use only 67 character
mapstr='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<>[]='
map=getmap(mapstr)
N=len(mapstr)

def encrypt(a, b, ptext):
    str=''
    for i in range(len(ptext)):
        try:
            p = map[ptext[i]]
            j = ((a ** i) * p + i*b) % N
            str=str+mapstr[j]
        except KeyError:
            str=str+ptext[i]
    return str

def decrypt(a, b, ctext):
    str=''
    for i in range(len(ctext)):
        try:
            c = map[ctext[i]]
            k = inverse((a**i) % N, N) 
            j = ((c - i*b) * k) % N
            str=str+mapstr[j]
        except KeyError:
            str=str+ctext[i]
    return str

def encrypt_file(a, b, fname):
    ptext=''
    with open(fname, "r") as f:
        ptext=f.read()
    return encrypt(a,b,ptext)

def decrypt_file(a, b, fname):
    ctext=''
    with open(fname, "r") as f:
        ctext=f.read()
    return decrypt(a,b,ctext)

def main(): 
    if len(sys.argv) < 6:
        print("Usage: python3 " + sys.argv[0] + " op key1 key2 infile outfile ")
        print("where op is either enc or dec")
        quit()
    op = sys.argv[1]
    key1 = int(sys.argv[2])
    key2  = int(sys.argv[3])
    infile  = sys.argv[4]
    outfile = sys.argv[5]
    
    if op == 'enc':
        text=encrypt_file(key1,key2,infile)
        with open(outfile, "w") as f:
            f.write(text)
    elif op == 'dec':
        text=decrypt_file(key1,key2,infile)
        with open(outfile, "w") as f:
            f.write(text)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
   

