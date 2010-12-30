import unittest
from should_dsl import should

from django.test import Client

class TesteGeral(unittest.TestCase):
    def test_deve_estar_disponivel_url_index(self):
        client = Client()
        response = client.post('/')
        response.status_code |should| equal_to(200)
