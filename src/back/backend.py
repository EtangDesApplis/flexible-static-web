from flask import Flask, request
from flask_cors import CORS
import time
import os
from pymongo import MongoClient
from random import randint
import pprint

app = Flask(__name__)
CORS(app)

#connection = MongoClient("myk3s.com",32017)
connection = MongoClient("mongodb")
db=connection['chefphan']


@app.route('/create/', methods=['POST'])
def makeOrder():
    #print(request.method)
    try:
      data = request.get_json()
      pprint.pprint(data)
      # processing
      collection=db["order"]
      collection.insert_one(data)
      return {"Status":"OK"}
    except:
      return {"Status":"KO"}

@app.route('/read/')
def listOrder():
    collection=db["order"]
    res={}
    i=1
    for doc in collection.find():
        pprint.pprint(doc)
        try:
            res[i]={"name":doc["name"],"phone":doc["phone"]}
            i=i+1
        except:
            pass
    return res

if __name__=="__main__":
  #to test with curl: curl localhost:5000 -d "{\"foo\": \"ok\"}" -H 'Content-Type: application/json'
  app.run(host='0.0.0.0')