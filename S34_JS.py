import requests
import json
import hashlib
import random
import time

def get_ts():
    ts = int(time.time()*1000)
    #print(ts)
    return ts

def get_bv():
    appVersion = 'Mozilla / 5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/86.0.4240.111 Safari/537.36'
    m=hashlib.md5()
    m.update(appVersion.encode('utf-8'))
    bv=m.hexdigest()
    #print(bv)
    return bv

def get_salt(ts):
    num = int(random.random()*10)
    salt = str(ts) + str(num)
    #print(salt)
    return salt

def get_sign(salt):
    a = 'fanyideskweb'
    b = '小帅b'
    c = salt
    d = ''

    str_data = a + b + str(c) + d

    m = hashlib.md5()
    m.update(str_data.encode('utf-8'))
    sign = m.hexdigest()
    #print(sign)

    return sign

def get_form_data(words=None):
    text = input(">>>")
    ts = get_ts()
    salt = get_salt(ts)

    form_data={
        'i': text,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        "salt": str(salt),
        "sign": get_sign(salt),
        "ts": str(ts),
        "bv": get_bv(),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        #'typeResult': 'false'
    }

    return form_data

def get_translate_date(word=None):
    form_data=get_form_data()
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    proxies = {
        "http":"http://10.10.1.10:3128",
        "https":"http://10.10.1.10:1080",
    }
    response = requests.post(url,data=form_data)
    content = json.loads(response.text)
    print(content['translateResult'][0][0]['tgt'])
if __name__ == '__main__':
    #a = input(">>>")
    get_translate_date()