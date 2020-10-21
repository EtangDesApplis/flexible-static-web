from pymongo import MongoClient
from random import randint
import pprint

client = MongoClient("myk3s.com",32017)
db=client['chefphan']
collection=db["order"]
# populate database
for i in range(10):
  #collection.insert_one({"name":"client%d"%(i),"item":"cake%d"%(randint(1,4))})
  collection.insert_one({"user":"client%d"%(i),"phone":"%d"%(randint(1,1000))})

# print out new database
for doc in collection.find():
    pprint.pprint(doc)
