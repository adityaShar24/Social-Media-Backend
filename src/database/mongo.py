from pymongo import MongoClient
from models.user_model import schema as user_schema
from models.posts_model import schema as posts_schema
from database.models.request_model import schema as request_schema
from database.models.comment_model import schema as comments_schema   
from utils.constants import CONNECTED_TO_MONGODB , CONNECTION_FAILED

MONGO_CONNECTION_STRING = 'mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority'

mongo_client = MongoClient(MONGO_CONNECTION_STRING)

database = mongo_client['Social-Media']
users_collection = database.create_collection('Users', { "validator":{ "$jsonSchema": user_schema } })
request_collection = database.create_collection('Requests', { "validator": { "$jsonSchema": request_schema } })
posts_collection = database.create_collection('Posts', { "validator": { "$jsonSchema": posts_schema } })
comments_collection = database.create_collection('Comments', { "validator": { "$jsonSchema": comments_schema } })


try:
    mongo_client.server_info()
    print(CONNECTED_TO_MONGODB)
except Exception as e:
    print(e , CONNECTION_FAILED)
    