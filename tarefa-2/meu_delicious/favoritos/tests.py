import unittest
from should_dsl import should

from django.test import Client

FIXTURES = 'fixtures.json'

class TesteRota(unittest.TestCase):

    fixtures = FIXTURES
    def setUp(self):
        self.client = Client()

    def test_url_index_disponivel(self):
        response = self.client.post('/')
        response.status_code |should| equal_to(200)

    def test_url_login_disponivel(self):
        response = self.client.post('/login/', {'username': 'admin', 'password': 'admin'})
        response.status_code |should| equal_to(200)
        
    def test_url_logout_disponivel(self):
        response = self.client.post('/logout/')
        response.status_code |should| equal_to(200)

    def test_url_cadastro_disponivel(self):
        response = self.client.post("/cadastrar/", {'username': 'tarsis', 'password1': 'tarsis ', 'password2': 'tarsis', 'email': 'tarsis.azevedo@gmail.com', 'first_name': 'Tarsis', 'last_name': 'Azevedo'})
        response.status_code |should| equal_to(200)

    def test_url_pessoal_disponivel(self):
        response = self.client.post("/meu_delicious/")
        response.status_code |should| equal_to(200)        