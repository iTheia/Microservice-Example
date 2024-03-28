from lib.base_repository import BaseRepository
from modules.clients.model import Client

"""
    TODO: proteger campos especificos por entidad que no deberian ser poder editados
"""
class ClientsRepository(BaseRepository):
    def __init__(self):
        super().__init__(Client)