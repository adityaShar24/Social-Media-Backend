from database.mongo import posts_collection
from .abstract_repository import AbstractRepository

class PostsRepository(AbstractRepository):
    def __init__(self):
        super().__init__(posts_collection)