#! -*- coding=utf-8 -*-

import requests
import os
import re
from bs4 import BeautifulSoup
import lxml


_url = 'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
urls = [_url.format(page=page) for page in range(1, 4328+1)]

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    img_list = soup.find_all('img', class_='ui image lazy')

    for img in img_list:
        image = img.get('data-original')
        title = img.get('title')
        # print(image)
        path = 'E:/00workspace/data/emoji/'
        try:
            with open(path + title + os.path.splitext(image)[-1], 'wb') as f:
                img = requests.get(image).content
                f.write(img)
        except:
            print("未知错误，继续运行")