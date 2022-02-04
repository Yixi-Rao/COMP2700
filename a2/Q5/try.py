from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.strxor import *
from Crypto.Util.Padding import pad

with open("Q5/sample.txt", "rb") as f:
    pt = f.read()
    
with open("Q5/sample.enc", "rb") as f:
    sample = f.read()
    
with open("Q5/flag.enc", "rb") as f:
    flag = f.read()
    
for i in range(len(sample) // 16):
    print(f'{sample[i * 16 : (i + 1) * 16].hex()} map with: {pt[i * 16 : (i + 1) * 16]}')
    # for i in range(num_boc):
    #     s = i * 16 + w
    #     if ct_w == sample[s : s + 1] :
    #         print(f'{sample[s : s + 1].hex()} == {pt[s : s + 1]}')
    #         result = result + str(pt[s : s + 1], encoding = "utf-8")
    #         break
    #     if i == num_boc - 1:
    #         print(f'{ct_w.hex()} == Cannot find the plaint text')
