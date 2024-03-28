from modules.clients.controller import ClientsController
import unittest
from unittest.mock import MagicMock, patch
from flask import Flask

class TestClientsController(unittest.TestCase):
    def setUp(self):
        self.clients_service_mock = MagicMock()
        self.controller = ClientsController(service=self.clients_service_mock)

    def test_get_all(self):
        with patch('flask.request') as request_mock:
            request_mock.args = {'page': 1, 'limit': 10}
            self.clients_service_mock.get_all.return_value = [{'id': 1, 'name': 'Client 1'}, {'id': 2, 'name': 'Client 2'}]
            response = self.controller.get_all()
            self.clients_service_mock.get_all.assert_called_once_with({'page': 1, 'limit': 10})
            self.assertEqual(response.status_code, 200)

    def test_get_by_id(self):
        with patch('flask.request') as request_mock:
            request_mock.args = {'id': 1}
            self.clients_service_mock.get_by_id.return_value = {'id': 1, 'name': 'Client 1'}
            response = self.controller.get_by_id(1)
            self.clients_service_mock.get_by_id.assert_called_once_with(1)
            self.assertEqual(response.status_code, 200)

    def test_create(self):
        with patch('flask.request') as request_mock:
            request_mock.json = {'name': 'New Client'}
            response = self.controller.create()
            self.clients_service_mock.create.assert_called_once_with({'name': 'New Client'})
            self.assertEqual(response.status_code, 200)

    def test_update(self):
        with patch('flask.request') as request_mock:
            request_mock.json = {'name': 'Updated Client'}
            response = self.controller.update(1)
            self.clients_service_mock.update.assert_called_once_with(1, {'name': 'Updated Client'})
            self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.controller.delete(1)
        self.clients_service_mock.delete.assert_called_once_with(1)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()