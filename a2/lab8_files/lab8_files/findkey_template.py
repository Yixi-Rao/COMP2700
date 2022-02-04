from Crypto.Util.number import *
from Crypto.Util.strxor import *

# read the encrypted document to bytes ct
with open('doc.enc', 'rb') as f:
    ct = f.read()

# known plaintext. 
known_pt = b'<html>'

# TODO: use the known plaintext to find S1, S2 and S3

# S1 = 
# S2 =
# S3 = 

# TODO: calculate the key (S0, A, B) using S1, S2 and S3
# A = 
# B =
# S0 = 

print("The key is (S0 = %d, A = %d, B = %d)" % (S0, A, B))

# Now you can use the key to decrypt doc.enc using the provided lcgcipher.py.

