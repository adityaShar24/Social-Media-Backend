from bson.objectid import ObjectId

class AbstractRepository:
    def __init__(self, collection):
        self.collection = collection
        
    def create(self, data):
        return self.collection.insert_one(data).inserted_id
    
    def update_one(self, query, data):
        return self.collection.update_one(query, data)

    def find_one(self, query):
        return self.collection.find_one(query)
    
    def find_many(self, query={}):
        return self.collection.find(query)
    
    def find_by_id(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})
    
    def delete_one(self, query):
        return self.collection.delete_one(query)
    
    def find_one_and_delete(self, query):
        return self.collection.find_one_and_delete(query)