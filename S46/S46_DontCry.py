#-*- coding=utf-8 -*-
#爬取QQ音乐的周杰伦的《说好不哭》的评论
#有评论在回复其他评论这里没有做判断去重

import requests
import re
import json


files = open("jay.txt","a",encoding="utf-8")

for i in range(9414):
    url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg"
    headers = {
        'Connection': "keep-alive",
        'Accept': "application/json, text/javascript, */*; q=0.01",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        'Origin': "https://y.qq.com",
        'Sec-Fetch-Site': "same-site",
        'Sec-Fetch-Mode': "cors",
        'Sec-Fetch-Dest': "empty",
        'Referer': "https://y.qq.com/",
        'Accept-Language': "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
        'Cookie': "pgv_pvi=1154200576; pt_sms_phone=176******26; RK=VKZIsIxiQi; ptcz=df590f44a84f4e8dc4114809cdae05544a05317da8bfe3bae8231cc176ddb406; tvfe_boss_uuid=d6fa64dd86e30a10; pgv_pvid=9701037670; eas_sid=n11620P000s8t6E7A6p2Z3I6N1; LW_sid=g106j0A2Z2R4h9w8I3s2s7V5X5; LW_uid=v1e6E0l2S2b4k9K8L3L2F78578; LOLWebSet_AreaBindInfo_2779681700=%257B%2522areaid%2522%253A%25221%2522%252C%2522areaname%2522%253A%2522%25E8%2589%25BE%25E6%25AC%25A7%25E5%25B0%25BC%25E4%25BA%259A%2520%25E7%2594%25B5%25E4%25BF%25A1%2522%252C%2522sRoleId%2522%253A0%252C%2522roleid%2522%253A%25222779681700%2522%252C%2522rolename%2522%253A%2522%25E4%25B8%2580%25E5%2589%2591%25E5%2585%2589%25E5%25AF%2592%25E7%2581%25AC%25E5%258D%2581%25E4%25B9%259D%25E6%25B4%25B2%2522%252C%2522checkparam%2522%253A%2522lol%257Cyes%257C2779681700%257C1%257C2779681700*%257C%257C%257C%257C%2525E4%2525B8%252580%2525E5%252589%252591%2525E5%252585%252589%2525E5%2525AF%252592%2525E7%252581%2525AC%2525E5%25258D%252581%2525E4%2525B9%25259D%2525E6%2525B4%2525B2*%257C%257C%257C1602249900%257C%2522%252C%2522md5str%2522%253A%2522FC26BF652D8A3BAAC75069D7E8EF856A%2522%252C%2522roleareaid%2522%253A%25221%2522%252C%2522sPartition%2522%253A%25221%2522%257D; ied_qq=o0944947973; uin_cookie=o0944947973; ts_refer=cn.bing.com/; ts_uid=1133482924; o_cookie=944947973; pac_uid=1_944947973; yqq_stat=0; pgv_si=s9025693696; pgv_info=ssid=s4264266240; userAction=1; ts_last=y.qq.com/n/yqq/song/001qvvgF38HVc4.html",
        'cache-control': "no-cache",
        'Postman-Token': "a0ad3afb-121b-4765-b42d-edab34dd978a"
    }
    querystring = {
        "g_tk_new_20200303": "5381",
        "g_tk": "5381",
        "loginUin": "0",
        "hostUin": "0",
        "format": "json",
        "inCharset": "utf8",
        "outCharset": "GB2312",
        "notice": "0",
        "platform": "yqq.json",
        "needNewCode": "0",
        "cid": "205360772",
        "reqtype": "2",
        "biztype": "1",
        "topid": "237773700",
        "cmd": "8",
        "needmusiccrit": "0",
        "pagenum": "0",
        "pagesize": "25",
        "lasthotcommentid": "",
        "domain": "qq.com",
        "ct": "24",
        "cv": "10101010"
    }
    querystring["pagenum"] = str(i)
    querystring["lasthotcommentid"] = ""
    response = requests.request("GET",url,headers=headers,params=querystring)

    comment_json = json.loads(response.text)
    comment_list = comment_json['comment']['commentlist']
    last_comment = comment_list[24]
    last_comment_id = last_comment['commentid']
    try:
        for comment in comment_list:
            rootcommentcontent = comment['rootcommentcontent']
            complie = re.compile(r'\[em].*[/em].',re.S)
            files.write(rootcommentcontent + '\n')
            print('正在写入评论',rootcommentcontent)
    except:
        print("此条评论异常，跳过")
        files.write("此条评论异常，跳过" + '\n')

files.close()
