class AbstractRepository:
    def __init__(self, collection):
        self.collection = collection
        
    def create(self, data):
        return self.collection.insert_one(data).inserted_id
    
    def update_one(self, query, data):
        return self.collection.update_one(query, data)

    def find_one(self, query):
        return self.collection.find_one(query)
    
    def find_many(self, query):
        return self.collection.find(query)
    
    
    
    