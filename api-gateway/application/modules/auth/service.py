from providers.service import ServiceManager
import requests


class AuthService:

    def __init__ (self, service_manager = None):
        self.auth_service = service_manager if service_manager else ServiceManager().get_url("AUTH")

    def register(self, data):
        response = requests.post("{}auth/register".format(self.auth_service), data)
        response.raise_for_status()
        return response.json()

    def login(self, data):
        response = requests.post("{}auth/login".format(self.auth_service), data)
        response.raise_for_status()
        return response.json()

    def renew_access_token(self, data):
        response = requests.post("{}auth/renew-access-token".format(self.auth_service), {
            'refreshToken': data
        })
        response.raise_for_status()
        return response.json()
