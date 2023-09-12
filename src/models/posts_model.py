from database.mongo import posts_collection , users_collection
from bson.objectid import ObjectId
class Posts:
    def __init__(self, url, caption, userId , likes=0):
        self.url = url
        self.likes = likes
        self.caption = caption
        self.userId = ObjectId(userId)
        self.comments = []

    def save_posts(self):
        saved_posts = posts_collection.insert_one({'url':self.url , 'likes':self.likes , 'caption':self.caption , 'userId':self.userId , 'comments':self.comments})
        return saved_posts
    
    def add_posts(postId , userId):
        post = users_collection.update_one({"_id": ObjectId(userId)}, { "$push": { "posts": postId}})
        return post
        
        
        
        