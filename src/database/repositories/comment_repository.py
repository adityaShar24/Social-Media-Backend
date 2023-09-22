from database.mongo import comments_collection
from .abstract_repository import AbstractRepository

class CommentsRepository(AbstractRepository):
    def __init__(self):
        super().__init__(comments_collection)
