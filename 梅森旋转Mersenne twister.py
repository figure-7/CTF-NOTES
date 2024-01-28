from hashlib import *
from itertools import *
from binascii import hexlify , unhexlify

from flag import flag ,seed

assert len(flag) == 26
assert flag[:7] == 'npuctf{'
assert flag[-1] == '}'

XOR = lambda s1 ,s2 : bytes([x1 ^ x2 for x1 ,x2 in zip(s1 , s2)])

class mt73991:
    def __init__(self , seed):
        self.state = [seed] + [0] * 232
        self.flag = 0
        self.srand()
        self.generate()
    def srand(self):
        for i in range(232):
            self.state[i+1] = 1812433253 * (self.state[i] ^ (self.state[i] >> 27)) - i
            self.state[i+1] &= 0xffffffff


    def generate(self):
        for i in range(233):
            y = (self.state[i] & 0x80000000) | (self.state[(i+1)%233] & 0x7fffffff)
            temp = y >> 1
            temp ^= self.state[(i + 130) % 233]
            if y & 1:
                temp ^= 0x9908f23f
            self.state[i] = temp
    def getramdanbits(self):
        if self.flag == 233:
            self.generate()
            self.flag = 0
        bits = self.Next(self.state[self.flag]).to_bytes(4 , 'big')
        self.flag += 1
        return bits
        
    def Next(self , tmp):
        tmp ^= (tmp >> 11)
        tmp ^= (tmp << 7) & 0x9ddf4680
        tmp ^= (tmp << 15) & 0xefc65400
        tmp ^= (tmp >> 18) & 0x34adf670
        return tmp

def encrypt(key , plain):
    tmp = md5(plain).digest()
    return hexlify(XOR(tmp , key))

if __name__ == "__main__":
    flag = flag.encode()
    random = mt73991(seed)
    f = open('./cipher.txt' , 'wb')
    for i in flag:
        key = b''.join([random.getramdanbits() for _ in range(4)])
        cipher = encrypt(key , chr(i).encode())
        f.write(cipher)





#cipher.txt
cef4876036ee8b55aa59bca043725bf350a5e491debdef7ef7d63e9609a288ca1e2c82a7fe566bd8709e73c8d495ea504a486ed11189faf8e6fb35617e47d2d1ad5e4783e96afeaae9f7104ec477fb39fe4ec619bf58289709e15c4449f03fc51cba918cd0ebfdc12376b41e7815406482733b3b200826b6c78d86563edaea94dccf459a4291517a4b8367d7b4a53aeecd7e0accf661bfc726f5ba62e1c0e04100108ad32e7d5711f780185cba5cf31d328bee84066be4ab9582cf9d4bfe3c6f96a7732e1c37d800c90fd46277147f0a26c149dcd5eeb0f2df0c075627bc220be5eefdd67186056ac28c21e155a7f247664aaecdb498134de274df10114d1f06f84dd21820f150d69c9439d909dec0f5ccfeab61b62db2ea91d31bc8163ff16c7f458006bd5ac4a5f5bfae2770b23ccfb7195b76aa0a9aa146831667a7b9fe08c19e691afadccb3ca5169ef3fabaa3dad47d536e89ed4cee6f788bc969c3ad3137850ebfc46a73af2b0c036c3da4b4a16506f499445c604dd73eeb846a52f881515a3ad0ab448b4f9ed3e0ab1fffac60b223dde6450ba6198e90e14de107aaf2





#python脚本
from Crypto.Hash import MD5
from hashlib import *
from itertools import *
from binascii import hexlify, unhexlify
from Crypto.Util import number
import string

cipher='cef4876036ee8b55aa59bca043725bf350a5e491debdef7ef7d63e9609a288ca1e2c82a7fe5'
#没有写全是因为只需要前32位.
plain='n'
plainmd5=MD5.new(plain.encode()).hexdigest()
m1=eval('0x'+plainmd5[:8])^eval('0x'+cipher[:8])
#print(m1)
m1=bin(m1)[2:].zfill(32)

def reverse1(x):
    x1=x[:18]
    tmp=eval('0b'+x[:14])&(eval('0b'+bin(0x34adf670)[2:][-14:]))
    x2=eval('0b'+x[-14:])^tmp
    x2=bin(x2)[2:].zfill(14)
    return x1+x2
def reverse2(x):
    x2=x[-15:]
    x1=(eval('0b'+x2)&eval('0b'+bin(0xefc65400)[2:][2:17]))^eval('0b'+x[2:17])
    tmp=eval('0b'+bin(x1)[-2:])&eval('0b'+bin(0xefc65400)[2:][:2])^eval('0b'+x[:2])
    return bin(tmp)[2:].zfill(2)+bin(x1)[2:].zfill(15)+x2
def reverse3(x):
    x3=x[-7:]
    x2=(eval('0b'+x3)&eval('0b'+bin(0x9ddf4680)[2:][-14:-7]))^eval('0b'+x[-14:-7])
    x1=(x2&eval('0b'+bin(0x9ddf4680)[2:][-21:-14]))^eval('0b'+x[-21:-14])
    x0=(x1&eval('0b'+bin(0x9ddf4680)[2:][-28:-21]))^eval('0b'+x[-28:-21])
    tmp=bin(x0)[2:].zfill(7)+bin(x1)[2:].zfill(7)+bin(x2)[2:].zfill(7)+x3
    ans=(eval('0b'+tmp[3:28]+'0000000')&0x9ddf4680)^eval('0b'+x)
    return bin(ans)[2:].zfill(32)
def reverse4(x):
    x1=x[:11]
    x2=eval('0b'+x1)^eval('0b'+x[11:22])
    tmp='00000000000'+(x1+bin(x2)[2:].zfill(11))[:21]
    ans=eval('0b'+tmp)^eval('0b'+x)
    return bin(ans)[2:].zfill(32)
    
res=m1
for i in range(1,5):
    res=eval('reverse'+str(i)+'(res)')
#print(eval('0b'+res))
seed = 1668245885

XOR = lambda s1, s2: bytes([x1 ^ x2 for x1, x2 in zip(s1, s2)])

class mt73991:
    def __init__(self, seed):
        self.state = [seed] + [0] * 232
        self.flag = 0
        self.srand()
        self.generate()
    def srand(self):
        for i in range(232):
            self.state[i + 1] = 1812433253 * (self.state[i] ^ (self.state[i] >> 27)) - i
            self.state[i + 1] &= 0xffffffff

    def generate(self):
        for i in range(233):
            y = (self.state[i] & 0x80000000) | (self.state[(i + 1) % 233] & 0x7fffffff)
            temp = y >> 1
            temp ^= self.state[(i + 130) % 233]
            if y & 1:
                temp ^= 0x9908f23f
            self.state[i] = temp

    def getramdanbits(self):
        if self.flag == 233:
            self.generate()
            self.flag = 0
        bits = self.Next(self.state[self.flag]).to_bytes(4, 'big')
        self.flag += 1
        return bits

    def Next(self, tmp):
        tmp ^= (tmp >> 11)
        tmp ^= (tmp << 7) & 0x9ddf4680
        tmp ^= (tmp << 15) & 0xefc65400
        tmp ^= (tmp >> 18) & 0x34adf670
        return tmp
        
def encrypt(key, plain):
    tmp = md5(plain).digest()
    return hexlify(XOR(tmp, key))
    
crypto=mt73991(seed)
f=open('cipher.txt','r').read()

s=string.printable
dic={}
for i in s:
    temp=MD5.new(i.encode()).hexdigest()
    dic[temp]=i
    
flag=''
for i in range(0,len(f),32):
    temp=f[i:i+32]
    key=b''.join([crypto.getramdanbits() for _ in range(4)])
    tempnum=number.bytes_to_long(key)
    tempmd5=eval('0x'+temp)^tempnum
    tempmd5=hex(tempmd5)[2:].zfill(32)
    flag+=dic[tempmd5]
print(flag)
