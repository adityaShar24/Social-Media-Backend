from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from .models.user_model import schema as user_schema
from .models.posts_model import schema as posts_schema
from .models.request_model import schema as request_schema
from .models.comment_model import schema as comments_schema
from .models.room_model import schema as rooms_schema
from .models.message_model import schema as messages_schema
from utils.constants import CONNECTED_TO_MONGODB, CONNECTION_FAILED

MONGO_CONNECTION_STRING = 'mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/'

def create_collection(database, collection_name, schema):
    if collection_name in database.list_collection_names():
        return database[collection_name]
    else:
        return database.create_collection(collection_name, **{"validator": {"$jsonSchema": schema}})

try:
    mongo_client = MongoClient(MONGO_CONNECTION_STRING, serverSelectionTimeoutMS=5000)
    mongo_client.server_info()  # Check if the server is reachable
    print(CONNECTED_TO_MONGODB)

    database = mongo_client['Social-Media']

    users_collection = create_collection(database, 'Users', user_schema)
    request_collection = create_collection(database, 'Requests', request_schema)
    posts_collection = create_collection(database, 'Posts', posts_schema)
    comments_collection = create_collection(database, 'Comments', comments_schema)
    rooms_collection = create_collection(database, 'Rooms', rooms_schema)
    messages_collection = create_collection(database, 'Messages', messages_schema)

except ServerSelectionTimeoutError as e:
    print(CONNECTION_FAILED, e)

