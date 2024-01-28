from pwn import *
import random
 
fw = open("1.log","wb")
dire = [b"W",b"A",b"S",b"D"]
while(1):
    try:
        io = remote("202.112.238.82", 13370)
        text = io.recvuntil(b"if you touch them.\n")
        fw.write(text)
        while(1):
            text = io.recvuntil("> ")
            fw.write(text)
            d = random.choice(dire)
            io.sendline(d)
            fw.write(d)
            fw.write(text)
            if(b"flag" in text):
                print(text)
    except:
        continue
