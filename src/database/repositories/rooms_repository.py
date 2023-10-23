from database.mongo import rooms_collection
from .abstract_repository import AbstractRepository

class RoomsRepository(AbstractRepository):
    def __init__(self):
        super().__init__(rooms_collection)