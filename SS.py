
#!/usr/bin/env python3
# encoding: utf-8

import os
import sys
import logging
import hashlib

from Crypto.Cipher import AES

logging.basicConfig(level=logging.INFO)


def EVP_BytesToKey(password, key_len, iv_len):
    m = []
    i = 0
    while len(b''.join(m)) < (key_len + iv_len):
        md5 = hashlib.md5()
        data = password
        if i > 0:
            data = m[i - 1] + password
        md5.update(data)
        m.append(md5.digest())
        i += 1
    ms = b''.join(m)
    key = ms[:key_len]
    iv = ms[key_len:key_len + iv_len]

    return key, iv

def decrypt(cipher,password):
    key_len = int(256/8)
    iv_len = 16
    mode = AES.MODE_CFB

    key, _ = EVP_BytesToKey(password, key_len, iv_len)
    cipher = bytes.fromhex(cipher)
    iv = cipher[:iv_len]
    real_cipher = cipher[iv_len:]

    obj = AES.new(key, mode, iv, segment_size=128)
    plain = obj.decrypt(real_cipher)

    return plain


def main():
    # test http request
    cipher = 'e0a77dfafb6948728ef45033116b34fc855e7ac8570caed829ca9b4c32c2f6f79184e333445c6027e18a6b53253dca03c6c464b8289cb7a16aa1766e6a0325ee842f9a766b81039fe50c5da12dfaa89eacce17b11ba9748899b49b071851040245fa5ea1312180def3d7c0f5af6973433544a8a342e8fcd2b1759086ead124e39a8b3e2f6dc5d56ad7e8548569eae98ec363f87930d4af80e984d0103036a91be4ad76f0cfb00206'

    with open('rockyou.txt','rb') as f:
        lines = f.readlines()
    for password in lines:
        plain = decrypt(cipher,password.strip())
        if b'HTTP' in plain:
            print(password,plain)

if __name__ == "__main__":
    main()
