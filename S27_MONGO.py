from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017/')

db = conn.avIdol

# db.col.insert({"name": '波多野結衣', 'bwh': '{ "b": 90, "w": 59, "h": 85}' , 'age': 30})
# db.col.insert([
#     {"name": '波多野結衣', 'bwh': '{ "b": 90, "w": 59, "h": 85}' , 'age': 30},
#     {"name": '吉泽明步', 'bwh': '{ "b": 86, "w": 58, "h": 86}' , 'age': 35},
#     {"name": '桃乃木香奈', 'bwh': '{ "b": 80, "w": 54, "h": 80}' , 'age': 22},
#     {"name": '西宫梦', 'bwh': '{ "b": 85, "w": 56, "h": 86}' , 'age': 22},
#     {"name": '松下纱荣子', 'bwh': '{ "b": 88, "w": 57, "h": 86}' , 'age': 28}
# ])
# print(db.col.find_one())

# db.col.find({"_id": ObjectId("5f71990712f9711c92098f5e")})
# db.col.find({"_id": "5f71990712f9711c92098f5e"})
# db.col.remove({"name": "波多野結衣"})
db.col.update({'name': '吉泽明步'}, {'$set': {'name': '苍井空'}})
# for item in db.col.find():
#     print(item)