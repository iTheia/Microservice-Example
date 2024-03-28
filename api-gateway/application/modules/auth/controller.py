from flask import jsonify, request, make_response
from modules.auth.service import AuthService

class AuthController:
    def __init__(self, service=None):
        self.service = service if service else AuthService()

    def register(self):
        credentials = request.json
        tokens = self.service.register(credentials)
        response = make_response(jsonify({'access': tokens['access']}))
        response.set_cookie('x-refresh-token', tokens['refresh'])
        return response

    def login(self):
        credentials = request.json
        tokens = self.service.login(credentials)
        response = make_response(jsonify({'access': tokens['access']}))
        response.set_cookie('x-refresh-token', tokens['refresh'])
        return response

    def renew_access_token(self):
        refresh_token = request.cookies.get('x-refresh-token')
        tokens = self.service.renew_access_token(refresh_token)
        return jsonify({'access': tokens['access']})
