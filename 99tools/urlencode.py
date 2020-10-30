from urllib.parse import urlencode

start_url='http://tieba.baidu.com/f?'
urldata = {
    'kw':'诗人李白',
    'ie':'utf-8',
    'pn':'100',
}

print(start_url+urlencode(urldata))