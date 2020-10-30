import requests
import re
from fontTools.ttLib import TTFont
import os
import xml.dom.minidom as xmldom
#获取字体下载url
def get_url():
    url = 'https://maoyan.com/board/1'
    headers = {
        'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/86.0.4240.111 Safari/537.36',
        'Cookie':'__mta=107191741.1602835854858.1603957073266.1603961124658.23; uuid_n_v=v1; uuid=3A7BDE100F8711EBBFF0EDDBFC80D58083CA62FF1F854148BA2CA679F7A7B4EE; _lxsdk_cuid=1753076336525-0109a318bb0f71-c781f38-1fa400-17530763366c8; _lxsdk=3A7BDE100F8711EBBFF0EDDBFC80D58083CA62FF1F854148BA2CA679F7A7B4EE; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; __mta=107191741.1602835854858.1603691674304.1603691685143.13; _csrf=82cfa51d7bb97ff2d8eeb91d3f7487cb1c0125f757d56a3c056f1bd99e99f262; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1603517847,1603691627,1603696934,1603957073; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1603961123; _lxsdk_s=17573886d93-226-a14-c21%7C%7C2'
    }
    html = requests.get(url=url,headers=headers).text
    #print(html)
    font_file_name = re.findall(r'//vfile.meituan.net/colorstone/(\w+\.woff)', html)[0]
    url = 'http://vfile.meituan.net/colorstone/' + font_file_name
    # print(url)
    # print(font_file_name)
    return url,font_file_name
#下载字体
def download_woff(url,font_file_name):
    #固定命名，呆的一笔……
    # woff = requests.get(url)
    # with open("2.woff",'wb') as wofff:
    #     wofff.write(woff.content)
    #取消固定的命名，改为匹配当次文件名字保存
    test = requests.get(url)
    if os.path.exists('fonts/'+font_file_name):
        return font_num_dit
    with open('fonts/'+ font_file_name, 'wb') as testt:
        testt.write(test.content)
#把woff转换为可读的xml文件
def woff_xml(font_file_name):
    base_font = TTFont("fonts/"+font_file_name)
    # 转换成xml格式
    base_font.saveXML("fonts/"+font_file_name+".xml")
#猫眼字符库
font_num_dit = [
    {'code':'uniE06C','num':'1'},{'code':'uniE845','num':'4'},{'code':'uniE824','num':'9'},
    {'code':'uniE2BC','num':'6'},{'code':'uniE40C','num':'5'},{'code':'uniE40C','num':'5'},
    {'code':'uniE989','num':'7'},{'code':'uniEAD5','num':'0'},{'code':'uniEB90','num':'2'},
    {'code':'uniED28','num':'7'},{'code':'uniE114','num':'7'},{'code':'uniE180','num':'6'},
    {'code':'uniE628','num':'2'},{'code':'uniE8FB','num':'1'},{'code':'uniE948','num':'5'},
    {'code':'uniEDC1','num':'8'},{'code':'uniEE76','num':'4'},{'code':'uniF00C','num':'3'},
    {'code':'uniF54D','num':'0'},{'code':'uniF65F','num':'9'},{'code':'','num':''},
]

#解析xml提取出数字的编码
def get_num(font_file_name):
    xmlfilepath = os.path.abspath("fonts/"+font_file_name+".xml")
    print(xmlfilepath)
    domobj = xmldom.parse(xmlfilepath)
    elementobj = domobj.documentElement
    subElementObj = elementobj.getElementsByTagName("TTGlyph")
    for i in range(1, 11):
        num_code = subElementObj[i].getAttribute("name")
        return num_code
    #print(num_code)

#主程序，挨个调用子程序
def main():
    url,font_file_name = get_url()
    download_woff(url,font_file_name)
    woff_xml(font_file_name)
    num_code = get_num(font_file_name)
if __name__ == '__main__':
    main()