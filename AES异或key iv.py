#python3
from Crypto.Cipher import AES
import os
from gmpy2 import*
from Crypto.Util.number import*

xor = 3657491768215750635844958060963805125333761387746954618540958489914964573229
enc_flag = b'>]\xc1\xe5\x82/\x02\x7ft\xf1B\x8d\n\xc1\x95i'
out = long_to_bytes(xor)
# print(out)
key = out[:16]*2
# print(key)
iv = bytes_to_long(key[16:])^bytes_to_long(out[16:])
# print(iv)
iv = long_to_bytes(iv)
# print(iv)
aes = AES.new(key,AES.MODE_CBC,iv)
flag = aes.decrypt(enc_flag)
print(flag)
