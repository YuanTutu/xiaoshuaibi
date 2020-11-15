#-*- coding :utf-8 -*-

import requests

urllll = 'http://v5-dy-j.ixigua.com/17d2105b9e0a0a6ea123107a27959615/5fb0fbd4/video/tos/cn/tos-cn-ve-15/61db7d6fb312469fba15f4ed40026c8b/?a=1128&br=8934&bt=2978&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=2020111516573601019806209942325241&lr=aweme_search_suffix&mime_type=video_mp4&qs=0&rc=ajtyNmU1ZHU4eDMzPGkzM0ApaGdnPDo2NWU7Nzw3ZjNpZWdxb25wNF9hb2tfLS1hLTBzczUvX2EuXzUyMzMyXjQ1YjU6Yw%3D%3D&vl=&vr='


response = requests.get(url=urllll)
print(response)
with open('test.mp4', 'ab') as f:
    f.write(response.content)
    f.close()
