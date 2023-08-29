from database.mongo import users_collection

class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        self.request_sent = []
        self.request_received = []
        self.friends = []
    
    def add_request_id(self , From , to):
        self.request_sent.append(From)
        self.request_received.append(to)
        self.save_user()
        return self.request_sent and self.request_received
    
    def save_user(self):
        user_id = users_collection.insert_one({'username':self.username , 'password':self.password , 'friends': self.friends , 'request_sent': self.request_sent , 'request_received':self.request_received}).inserted_id
        return user_id
    
    def find_by_username(username):
        user = users_collection.find_one({'username':username})
        return user
    
