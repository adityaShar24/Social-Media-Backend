from database.mongo import messages_collection
from .abstract_repository import AbstractRepository

class MessagesRepository(AbstractRepository):
    def __init__(self):
        super().__init__(messages_collection)