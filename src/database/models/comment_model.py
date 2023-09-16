from database.mongo import comments_collection, posts_collection
from bson.objectid import ObjectId as Ob

class Comment:
    def __init__(self , comment , postId , userId , parent_commentId):
        self.comment = comment
        self.postId = postId    
        self.userId = userId
        self.parent_commentId = parent_commentId if parent_commentId else None
        
    def save_comments(self):
        commentID = comments_collection.insert_one({
            'comment' : self.comment,
            'postId' : self.postId,
            'userId' : self.userId,
            'parent_commentId' : self.parent_commentId
        }).inserted_id
        return commentID

        
    def add_commentId(postId , commentId):
        posts_collection.update_one({'_id' : Ob(postId)} , {'$push' : {'comments' : Ob(commentId) } } )
    