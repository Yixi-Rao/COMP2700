from Crypto.Cipher import AES
from Crypto.Util.strxor import *
from Crypto.Util.Padding import pad

IV = b'0123456789ab'

def encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CTR, nonce=IV)
    # apply PKCS#7 padding prior to encryption
    ct = cipher.encrypt(pad(data, AES.block_size))
    return ct