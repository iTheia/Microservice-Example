import unittest
from unittest.mock import MagicMock
from modules.clients.service import ClientsService

class TestClientsService(unittest.TestCase):
    def setUp(self):
        self.repository_mock = MagicMock()
        self.service = ClientsService(repository=self.repository_mock)

    def test_get_all(self):
        pager_options = {'page': 1, 'limit': 10}
        expected_result = [{'id': 1, 'name': 'Client 1'}, {'id': 2, 'name': 'Client 2'}]
        self.repository_mock.get_all.return_value = expected_result
        result = self.service.get_all(pager_options)
        self.repository_mock.get_all.assert_called_once_with(pager_options)
        self.assertEqual(result, expected_result)

    def test_get_by_id(self):
        client_id = 1
        expected_result = {'id': 1, 'name': 'Client 1'}
        self.repository_mock.get_by_id.return_value = expected_result
        result = self.service.get_by_id(client_id)
        self.repository_mock.get_by_id.assert_called_once_with(client_id)
        self.assertEqual(result, expected_result)

    def test_create(self):
        client_data = {'name': 'New Client'}
        self.service.create(client_data)
        self.repository_mock.create.assert_called_once_with(client_data)

    def test_update(self):
        client_id = 1
        client_data = {'name': 'Updated Client'}
        self.service.update(client_id, client_data)
        self.repository_mock.update.assert_called_once_with(client_id, client_data)

    def test_delete(self):
        client_id = 1
        self.service.delete(client_id)
        self.repository_mock.delete.assert_called_once_with(client_id)