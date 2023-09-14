from database.mongo import comments_collection, users_collection
from bson.objectid import ObjectId as Ob

class Comment:
    def __init__(self , comment , postId , userId , parent_commentId):
        self.comment = comment
        self.postId = postId    
        self.userId = userId
        self.parent_commentId = parent_commentId if parent_commentId else None
        
    def save_comments(self):
        comments_collection.insert_one({
            'comment' : self.comment,
            'postId' : self.postId,
            'userId' : self.userId,
            'parent_commentId' : self.parent_commentId
        })

        
    def add_commentId(userId , commentId):
        users_collection.update_one({'_id' : Ob(userId)} , {'$push' : {'comments' : commentId } } )
    