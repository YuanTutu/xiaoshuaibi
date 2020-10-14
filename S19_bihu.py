import requests

headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': '_zap=c9104379-2354-46ca-b993-7f11b76e63d2; _xsrf=fzLx85b8v2xXMYcKZPf3C8jnd6Q5ov1F; _ga=GA1.2.326157933.1591596156; d_c0="AFAadjW1ZBGPTvWjYNJgrNPk2vg6Nc2i-44=|1591596165"; tst=r; q_c1=e46ac715837845079f5ea5ff34ff9c77|1598942028000|1592399240000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1599039620,1599455464,1599455697,1599810298; _gid=GA1.2.1188359621.1599810314; SESSIONID=lQagWfDl1viFLGQnkMEPMrq9KvwQErzi85XPPgpdRsm; JOID=V1odCkLGavH5Z_2DDspx5wOeKQMSrTGRnjyczWP7G5K-K7bVatZQq6ps8IgPP-Xrfsn8y9YaJxbRpa42AIPfmec=; osd=VF8UBUzFb_j2af6GB8V_5AaXJg0RqDiekD-ZxGz1GJe3JLjWb99fpalp-YcBPODiccf_zt8VKRXUrKE4A4bWluk=; capsion_ticket="2|1:0|10:1599811882|14:capsion_ticket|44:ZDBlNjIyMjM5Njc1NDY4MGE2ZjMxOWZhYTUwNWZlZTI=|34c274798eabbb57498fb53bd958e2fdb9fd1ebca886dd1832c1c1a70808f49f"; z_c0="2|1:0|10:1599811890|4:z_c0|92:Mi4xZ0xlNkFBQUFBQUFBVUJwMk5iVmtFU1lBQUFCZ0FsVk5NbjlJWUFDcE9ZTjhua3NTaDMwWEtHVGU1WktxQU5EUDdR|47b881dceb691d5a0b966aee5d6b7c122e02d9f255099fe2138f957761549f42"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1599811883; KLBRSID=81978cf28cf03c58e07f705c156aa833|1599811940|159981029',
}

session = requests.Session()
response = session.get('https://www.zhihu.com/', headers=headers)

print(response.text)