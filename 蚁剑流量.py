import socket
from Crypto.Cipher import ARC4
import base64
import os
import json
import hashlib


def calculate_md5(string):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode('utf-8'))
    md5_hex = md5_hash.hexdigest()
    return md5_hex


from Crypto.Cipher import ARC4
import base64
import json

# with open("./s3creT.txt", "r") as f:
#     key = f.read()
key = "R@ns0mwar3_V1ru5"
key = calculate_md5(key)


def rc4_encrypt(data, key1):
    key = bytes(key1, encoding='utf-8')
    enc = ARC4.new(key)
    res = enc.encrypt(data.encode('utf-8'))
    res = base64.b64encode(res)
    res = str(res, 'utf-8')
    return res


def rc4_decrypt(data, key1):
    data = base64.b64decode(data)
    key = bytes(key1, encoding='utf-8')
    enc = ARC4.new(key)
    res = enc.decrypt(data)
    res = str(res, 'gbk', errors='ignore')
    return res


def t1(data, timestamp):
    import re
    from datetime import datetime, timedelta
    # current_time = datetime.now()
    current_time = datetime.fromtimestamp(timestamp)
    target_time = current_time.replace(second=0, microsecond=0)
    timestamp = int(target_time.timestamp())
    key1 = hex(timestamp)[2:].zfill(8)
    key1 = re.findall(r'.{2}', key1)
    key1 = [int(i, 16) for i in key1]
    data = list(data)
    for i in range(len(data)):
        data[i] = chr(ord(data[i]) ^ key1[i % 4])
    data = ''.join(data)
    return data


def decrypt(data, key, timestamp):
    data = t1(data, timestamp)
    data = rc4_decrypt(data, key)
    return data


def encrypt(data, key):
    data = rc4_encrypt(data, key)
    data = t1(data)

    return data


def system(cmd):
    res = os.popen(cmd).read()
    return res if res else "NoneResult"


def main():
    # ip = '192.168.31.42'
    # port = 8899
    # socket_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # socket_server.bind((ip, port))
    # socket_server.listen(1)
    # while True:
    #     conn, addr = socket_server.accept()
    #     with conn:
    #         print("connect::", addr)
    #         try:
    #             while True:
    #                 data = conn.recv(102400)
    #                 # print("server recevie peername and data:", conn.getpeername(), data.decode())
    #                 if data:
    #                     data = data.decode()
    #                     data = decrypt(data, key)
    #                     data = json.loads(data)
    #                     if data["opcode"] == "shell":
    #                         print("shellCMD::", data["msg"])
    #                         res = system(data["msg"])
    #                         print("res::", res)
    #                         conn.sendall(encrypt(res, key).encode())
    #                 else:
    #                     break
    #         except ConnectionResetError as e:
    #             print("猫驴聹莽篓聥猫驴聻忙聨楼忙聳颅氓录聙")

    data = "16c3b2c295c3be04c29cc29fc3a90cc39ec2a3c39937c391c3a7c3811cc38bc3a0c39b29c29ac2b1c3b830c3b2c286c3a13cc38ac296c38d13c3a2c29dc3920bc3bac2a8c2bb22c29bc287c3a328c3afc29cc3bd27c390c3a6c38110c381c2a5c381"
    timestamp = 1705562796.602401000
    data = bytes.fromhex(data)
    data = data.decode('utf-8')
    result = decrypt(data, key, timestamp)
    print(result)
    # data = json.loads(data)
    # if data["opcode"] == "shell":
    #     print("shellCMD::", data["msg"])
    #     res = system(data["msg"])
    #     print("res::", res)


if __name__ == '__main__':
    main()
    # 运行结果：flag{3741b40e-3185-4a9a-80a6-83403e4942fc}
