from scrapy.cmdline import execute
#普通的运行
execute(["scrapy","crawl","stackoverflow-python"])
#保存一个json
#execute(["scrapy","crawl","stackoverflow-python","-o","starrrr.json"])