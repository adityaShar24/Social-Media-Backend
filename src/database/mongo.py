from pymongo import MongoClient
from .models.user_model import schema as user_schema
from .models.posts_model import schema as posts_schema
from .models.request_model import schema as request_schema
from .models.comment_model import schema as comments_schema
from .models.room_model import schema as rooms_schema   
from .models.message_model import schema as messages_schema
from utils.constants import CONNECTED_TO_MONGODB , CONNECTION_FAILED

MONGO_CONNECTION_STRING = 'mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority'

mongo_client = MongoClient(MONGO_CONNECTION_STRING)

database = mongo_client['Social-Media']

users_collection = None
request_collection = None
posts_collection = None
comments_collection = None
rooms_collection = None
messages_collection = None

if 'Users' in database.list_collection_names():
    users_collection = database['Users']
else:
    users_collection = database.create_collection('Users' , **{ "validator": { "$jsonSchema": user_schema } })
    
if 'Requests' in database.list_collection_names():
    request_collection = database['Requests']
else:
    request_collection = database.create_collection('Requests' , **{ "validator": { "$jsonSchema": request_schema } })

# do the same for other collections
if 'Posts' in database.list_collection_names():
    posts_collection = database['Posts']
else:
    posts_collection = database.create_collection('Posts' , **{ "validator": { "$jsonSchema": posts_schema } })
    
if 'Comments' in database.list_collection_names():
    comments_collection = database['Comments']
else:
    comments_collection = database.create_collection('Comments' , **{ "validator": { "$jsonSchema": comments_schema } })
    
if 'Rooms' in database.list_collection_names():
    rooms_collection = database['Rooms']
else:
    rooms_collection = database.create_collection('Rooms' , **{ "validator": { "$jsonSchema": rooms_schema } })
    
if 'Messages' in database.list_collection_names():
    messages_collection = database['Messages']
else:
    messages_collection = database.create_collection('Messages' , **{ "validator": { "$jsonSchema": messages_schema } })

try:
    mongo_client.server_info()
    print(CONNECTED_TO_MONGODB)
except Exception as e:
    print(e , CONNECTION_FAILED)
    