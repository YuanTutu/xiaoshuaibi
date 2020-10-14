from flask import Flask,request
#import urllib.request
#import request

app = Flask(__name__)

@app.route('/getInfo',methods=["GET","POST"])
#http://127.0.0.1:5000/getInfo这样才可以访问，不能去掉端口
def hello_world():
    print(request.headers)#记得导入request模块
    head = request.headers.get('User-Agent')
    if (str(head).startswith('python')):
        return "小子，使用爬虫是吧？滚你的"
    else:
        return "这里假装有很多数据"
    #return "数据"

if __name__ == "__main__":
    app.run(debug=True)