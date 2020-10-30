from urllib.parse import unquote

name = 'https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail&dep=%E6%BE%B3%E9%97%A8&query=%E4%B8%89%E4%BA%9A%E8%87%AA%E7%94%B1%E8%A1%8C&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=dujia_hy_destination&date=&needNoResult=true&originalquery=%E4%B8%89%E4%BA%9A%E8%87%AA%E7%94%B1%E8%A1%8C&width=480&height=320&quality=90&limit=0,28&includeAD=true&qsact=search'
url_decode_name = unquote(name)
print(url_decode_name)

#Request URL: https://touch.dujia.qunar.com/list?modules=list%2CbookingInfo%2CactivityDetail&dep=%E6%BE%B3%E9%97%A8&query=%E4%B8%89%E4%BA%9A%E8%87%AA%E7%94%B1%E8%A1%8C&dappDealTrace=true&mobFunction=%E6%89%A9%E5%B1%95%E8%87%AA%E7%94%B1%E8%A1%8C&cfrom=zyx&it=dujia_hy_destination&date=&needNoResult=true&originalquery=%E4%B8%89%E4%BA%9A%E8%87%AA%E7%94%B1%E8%A1%8C&width=480&height=320&quality=90&limit=0,28&includeAD=true&qsact=search