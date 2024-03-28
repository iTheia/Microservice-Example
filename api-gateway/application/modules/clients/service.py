from modules.clients.repository import ClientsRepository
from modules.clients.serializer import serialize_clients, serialize_client

class ClientsService:
    def __init__(self, repository=None):
        self.repository = repository if repository else ClientsRepository()

    def get_all(self, pager_options):
        return serialize_clients(self.repository.get_all(pager_options))

    def get_by_id(self, id):
        return serialize_client(self.repository.get_by_id(id))

    def create(self, client):
        return self.repository.create(client)

    def update(self, id, client):
        return self.repository.update(id, client)

    def delete(self, id):
        return self.repository.delete(id)
