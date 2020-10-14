import pymysql
#连接数据库
db = pymysql.connect("127.0.0.1","root","123456","avidol")

cursor = db.cursor()
#创建数据库
# sql = """create table beautyGirls(
#     name char(20) not null,
#     age int)"""
# cursor.execute(sql)
#插入数据
sql = "insert into beautyGirls(name, age) values ('Mrs.cang', 18)"

try:
    cursor.execute(sql)
    db.commit()
except:
    # 回滚
    db.rollback()

db.close()