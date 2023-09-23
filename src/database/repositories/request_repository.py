from database.mongo import request_collection
from .abstract_repository import AbstractRepository

class RequestsRepository(AbstractRepository):
    def __init__(self):
        super().__init__(request_collection)