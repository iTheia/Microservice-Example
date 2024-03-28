from flask import jsonify, request
from modules.clients.service import ClientsService
from lib.pager import Pager

class ClientsController:
    def __init__(self, service=None):
        self.service = service if service else ClientsService()

    def get_all(self):
        pager = Pager(**request.args)
        pager_options = pager.paginate()
        clients = self.service.get_all(pager_options)
        return jsonify(clients)

    def get_by_id(self, id):
        client = self.service.get_by_id(id)
        return jsonify(client)

    def create(self):
        client = request.json
        self.service.create(client)
        return jsonify({"message": "Created successfully"})

    def update(self, id):
        update_body = request.json
        self.service.update(id, update_body)
        return jsonify({"message": "Updated successfully"})

    def delete(self, id):
        self.service.delete(id)
        return jsonify({"message": "Deleted successfully"})
