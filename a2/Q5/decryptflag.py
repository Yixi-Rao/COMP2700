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

result = ""
num_boc = len(sample) // 16
for w in range(32):
    ct_w = flag[w : w + 1]
    for i in range(num_boc):
        s = i * 16 + w
        if ct_w == sample[s : s + 1] :
            print(f'{sample[s : s + 1].hex()} == {pt[s : s + 1]}')
            result = result + str(pt[s : s + 1], encoding = "utf-8")
            break
        if i == num_boc - 1:
            print(f'Cannot find the plaint text')
            
print(result)

# print(badaes.AES.pad(AES,pt))

# a = 9f
# f = a7
# l = 9c
# e = 45
# c = 46
# a7 5c 75 b6 58 b1 89 ae 78 4e 4d 12 e7 41 61 bd
# f  l  a  g  {  l
#a75c75b658b189ae784e4d12e74161bd

