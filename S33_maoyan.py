import requests
import re
from fontTools.ttLib import TTFont

#获取字体下载url
def get_url():
    url = 'https://maoyan.com/board/1'
    headers = {
        'User-Agent': 'Mozilla / 5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/86.0.4240.111 Safari/537.36',
        'Cookie':'__mta=107191741.1602835854858.1603691846160.1603696934234.19; uuid_n_v=v1; uuid=3A7BDE100F8711EBBFF0EDDBFC80D58083CA62FF1F854148BA2CA679F7A7B4EE; _lxsdk_cuid=1753076336525-0109a318bb0f71-c781f38-1fa400-17530763366c8; _lxsdk=3A7BDE100F8711EBBFF0EDDBFC80D58083CA62FF1F854148BA2CA679F7A7B4EE; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; __mta=107191741.1602835854858.1603691674304.1603691685143.13; _csrf=b8b24f12e6497b5d47548e7687edb08637d129f4b262903695852f584cc6ba5d; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1602835854,1603517847,1603691627,1603696934; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1603696934; _lxsdk_s=17563e9fd52-8d5-f86-9ff%7C%7C1'
    }
    html = requests.get(url=url,headers=headers).text
    #print(html)
    font_file_name = re.findall(r'//vfile.meituan.net/colorstone/(\w+\.woff)', html)[0]
    url = 'http://vfile.meituan.net/colorstone/' + font_file_name
    #print(url)
    return url

#下载字体
def download_woff(url):
    woff = requests.get(url)
    with open("2.woff",'wb') as wofff:
        wofff.write(woff.content)

#把woff转换为可读的xml文件
def woff_xml():
    base_font = TTFont("2.woff")
    # 转换成xml格式
    base_font.saveXML("2.xml")

#处理xml内容

#主程序，挨个调用子程序
def main():
    url = get_url()
    download_woff(url)
    woff_xml()


if __name__ == '__main__':
    main()