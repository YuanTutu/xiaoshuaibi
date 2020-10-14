import requests

url = 'http://127.0.0.1:5000/getInfo'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
response = requests.get(url,headers=headers)
print(response.text)