import requests
import re
import time

url = 'http://7ef8f829-d5ef-418b-8042-377151d37b69.node4.buuoj.cn:81/'
session = requests.session()
req = session.get(url).text
flag = ""

for i in range(1010):
    try:
        result = re.findall("\<br\>\<br\>(\d.*?)\<br\>\<br\>",req)#获取[数字]
        result = "".join(result)#提取字符串
        result = eval(result)#运算
        print("time: "+ str(i) +"   "+"result: "+ str(result))

        data = {"answer":result}
        req = session.post(url,data=data).text
        if "flag{" in req:
            print(re.search("flag{.*}", req).group(0)[:50])
            break
        time.sleep(0.1)#防止访问太快断开连接
    except:
        print("[-]")
