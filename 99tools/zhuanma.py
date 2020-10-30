from urllib.parse import quote

name = '北京'
url_encode_name = quote(name)
print(url_encode_name)