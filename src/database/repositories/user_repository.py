from database.mongo import users_collection
from .abstract_repository import AbstractRepository

class UserRepository(AbstractRepository):
    def __init__(self):
        super().__init__(users_collection)
        
