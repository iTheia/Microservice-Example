from flask import Flask
from modules.clients.controller import ClientsController
from modules.loans.controller import LoansController
from modules.auth.controller import AuthController
from middlewares.auth import jwt_required

def setup_routes(app: Flask):
    clients_controller = ClientsController()
    loans_controller = LoansController()
    auth_controller = AuthController()

    app.add_url_rule('/clients', 'get_all_clients', clients_controller.get_all, methods=['GET'])
    app.add_url_rule('/clients/<int:id>', 'get_client_by_id', clients_controller.get_by_id, methods=['GET'])
    app.add_url_rule('/clients', 'create_client', clients_controller.create, methods=['POST'])
    app.add_url_rule('/clients/<int:id>', 'update_client', clients_controller.update, methods=['PUT'])
    app.add_url_rule('/clients/<int:id>', 'delete_client', clients_controller.delete, methods=['DELETE'])

    app.add_url_rule('/loans', 'get_all_loans', jwt_required(loans_controller.get_all), methods=['GET'])
    app.add_url_rule('/loans/<int:id>', 'get_loan_by_id', jwt_required(loans_controller.get_by_id), methods=['GET'])
    app.add_url_rule('/loans', 'create_loan', jwt_required(loans_controller.create), methods=['POST'])
    app.add_url_rule('/loans/<int:id>', 'update_loan', jwt_required(loans_controller.update), methods=['PUT'])
    app.add_url_rule('/loans/<int:id>', 'delete_loan',jwt_required( loans_controller.delete), methods=['DELETE'])

    app.add_url_rule('/login', 'login', auth_controller.login, methods=['POST'])
    app.add_url_rule('/register', 'register', auth_controller.register, methods=['POST'])
    app.add_url_rule('/renew-access-token', 'renew_access_token', auth_controller.renew_access_token, methods=['POST'])

