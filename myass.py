from pymongo import MongoClient

client = MongoClient()
db = client.test

from datetime import datetime
result = db.restaurants.delete_many({})
# result = db.restaurants.insert_one(
#     {
#         "restaurant_id": "41704620"
#     }
# )
# cursor = db.restaurants.find()
# for document in cursor:
#     print(document)