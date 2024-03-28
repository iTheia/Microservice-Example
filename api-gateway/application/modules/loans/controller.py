from flask import jsonify, request
from modules.loans.service import LoansService
from lib.pager import Pager


class LoansController:
    def __init__(self, service=None):
        self.service = service if service else LoansService()

    def get_all(self):
        pager = Pager(**request.args)
        pager_options = pager.paginate()
        loans = self.service.get_all(pager_options)
        return jsonify(loans)

    def get_by_id(self, id):
        loan = self.service.get_by_id(id)
        return jsonify(loan)

    def create(self):
        payload = request.json
        loan = self.service.create(payload)
        return jsonify(loan)

    def update(self, id):
        update_body = request.json
        self.service.update(id, update_body)
        return jsonify({"message": "Updated successfully"})

    def delete(self, id):
        self.service.delete(id)
        return jsonify({"message": "Deleted successfully"})
