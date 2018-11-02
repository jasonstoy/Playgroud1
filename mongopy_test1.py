from pymongo import MongoClient
from pprint import pprint

uri = 'mongodb://Jason:<password>@cluster0-shard-00-00-opsao.mongodb.net:27017,cluster0-shard-00-01-opsao.mongodb.net:27017,cluster0-shard-00-02-opsao.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true'
client = MongoClient(uri)
db = client['test']
collection = db['test1']
cursor = collection.find({})
for data in cursor:
    pprint(data)
