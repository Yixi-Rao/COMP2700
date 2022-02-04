from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.strxor import *
from Crypto.Util.Padding import pad

def cfbAES(data):
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    l = len(data)

    if l >= (2 ** 32):
        print("Input too long")
        raise ValueError
    
    lb = long_to_bytes(l, 4)

    data = pad(data+lb, 32)
    ct = cipher.encrypt(data)
    return ct

with open("Q6/fst.bin", "rb") as f:
    data = f.read()

key = b'AES-HASH-1234567'
iv  = b'0123456789abcdef'

ori_ct = cfbAES(data)

y1 = ori_ct[0:16]
y2 = ori_ct[16:32]
y3 = ori_ct[32:48]
y4 = ori_ct[48:]

print(y1.hex())
print(y2.hex())
print(y3.hex())
print(y4.hex())

cipher = AES.new(key, mode=AES.MODE_ECB)

m1 = strxor(cipher.decrypt(y1), cipher.encrypt(iv))
m2 = strxor(y1, cipher.decrypt(y2))
m3 = strxor(y2, y3)

m  = m1 + m2 + m3
with open("Q6/snd.bin",'wb') as f:
    f.write(m)
    
print("testing whether new_m == ori_m: " + str(m == data))
print("--------------------------------------------------------")

with open("Q6/snd.bin",'rb') as f:
    rm = f.read()
new_ct = cfbAES(rm)

y1_snd = new_ct[0:16]
y2_snd = new_ct[16:32]
y3_snd = new_ct[32:48]
y4_snd = new_ct[48:]

print(y1_snd.hex())
print(y2_snd.hex())
print(y3_snd.hex())
print(y4_snd.hex())

print("----------------------------testing----------------------")
print(f'y1 != y1_snd -> {y1 == y1_snd}')
print(f'y2 != y2_snd -> {y2 == y2_snd}')
print(f'y3 == y3_snd -> {y3 == y3_snd}')
print(f'y4 == y4_snd -> {y4 == y4_snd}')
