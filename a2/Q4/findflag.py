from Crypto.Util.number import *
from Crypto.Util.strxor import *
from Crypto.Cipher import AES


with open('Q4/cipher1.bin', 'rb') as f:
    flags = f.read()
    
with open('Q4/cipher2.bin', 'rb') as f:
    flag = f.read()
    
block_len = len(flags) // 16
# ref.txt is the orignal plain1.txt changed to be seperated by one space amoung flags
with open('Q4/ref.txt', 'r') as f:
    pt = f.read().split(' ')
    
for i in range(block_len):
    if i != 0:
        yi   = flags[i * 16 : (i + 1) * 16]
        yi_1 = flags[(i - 1) * 16 : i * 16]
        if (strxor(flag[0 : 16] ,flag[16 : 32]) == strxor(yi ,yi_1)):
            print(f'Done! E_k(x{i + 1}), with index {i}, flag: {pt[i]}')
            break
    if i == block_len - 1:
        print(f'Done! E_k(x{1}), with index {0}, flag: {pt[0]}')


   