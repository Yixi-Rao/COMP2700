from Crypto.Util.number import *
from Crypto.Util.strxor import *

import elcgcipher

with open('Q2/cipher.bin', 'rb') as f:
    ct = f.read()

known_pt = b'Now is a good time to buy stock.'

S = strxor(known_pt[0:10], ct[0:10])

S2 = bytes_to_long(S[0:2])
S3 = bytes_to_long(S[2:4])
S4 = bytes_to_long(S[4:6])
S5 = bytes_to_long(S[6:8])
S6 = bytes_to_long(S[8:10])

print("S2 = %d, S3 = %d, S4 = %d, S5 = %d, S6 = %d" % (S2,S3,S4,S5,S6))
print("------------------------------------------------------------------------")

B = (((S4 - S5) * inverse(S3 - S4, 64283) - (S5 - S6) * inverse(S4 - S5, 64283))
     * inverse((S2 - S3) * inverse(S3 - S4, 64283) - (S3 - S4) * inverse(S4 - S5, 64283), 64283)) % 64283
A = ((S4 - S5) * inverse(S3 - S4, 64283) - B * (S2 - S3)* inverse(S3 - S4, 64283)) % 64283
C  = (S4 - A * S3 - B * S2) % 64283
S1 = ((S3 - A * S2 - C) * inverse(B, 64283)) % 64283
S0 = ((S2 - A * S1 - C) * inverse(B, 64283)) % 64283

print("The key is (S0 = %d, S1 = %d, A = %d, B = %d, C = %d)" % (S0, S1, A, B, C))
print("------------------------------------------------------------------------")

elcgcipher.encfile(S0, S1, A, B, C, "Q2/cipher.bin", "Q2/pt.txt")