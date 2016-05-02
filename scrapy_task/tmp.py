# from datetime import datetime
# from elasticsearch import Elasticsearch
# es = Elasticsearch()
#
# doc = {
#     'author': 'autho2',
#     'text': 'text2.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index1", doc_type='tweet',  body=doc)
# print(res['created'])
# res = es.get(index="test-index1", doc_type='tweet', id=1)
# print(res['_source'])



import pymongo
import ssl

MONGODB_URL = 'mongodb://test_ivan:11111111@aws-us-east-1-portal \
    .11.dblayer.com:27790,aws-us-east-1-portal.10.dblayer.com:11140/bbc'
client = pymongo.MongoClient(MONGODB_URL)
db = client.get_default_database()
print db.collection_names()
