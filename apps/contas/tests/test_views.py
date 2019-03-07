import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from contas.models import Conta


class ContaAPIViewTestCase(APITestCase):
    url = reverse("lista")

    def setUp(self):
        self.username = "john"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        conta = Conta()
        conta.usuario = self.user
        conta.nome = 'Job'
        conta.valor = 2000
        conta.save()

        conta = Conta()
        conta.usuario = self.user
        conta.nome = 'Job'
        conta.valor = 1800
        conta.save()

        conta = Conta()
        conta.usuario = self.user
        conta.nome = 'Pagamento'
        conta.valor = -200
        conta.save()

        conta = Conta()
        conta.usuario = self.user
        conta.nome = 'Pagamento'
        conta.valor = -100
        conta.save()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_lista_contas(self):
        response = self.client.get(self.url)
        print(response.data)
        self.assertEqual(200, response.status_code)

    def test_lista_ordenar_nome_ascendente(self):

        response = self.client.get(self.url + '?ordering=nome')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['nome'], 'Job')
        self.assertEqual(data[-1]['nome'], 'Pagamento')

    def test_lista_ordenar_nome_descendente(self):

        response = self.client.get(self.url + '?ordering=-nome')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['nome'], 'Pagamento')
        self.assertEqual(data[-1]['nome'], 'Job')

    def test_lista_ordenar_valor_ascendente(self):

        response = self.client.get(self.url + '?ordering=valor')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['valor'], '-200.00')
        self.assertEqual(data[-1]['valor'], '2000.00')

    def test_lista_ordenar_valor_descendente(self):

        response = self.client.get(self.url + '?ordering=-valor')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['valor'], '2000.00')
        self.assertEqual(data[-1]['valor'], '-200.00')

    def test_lista_ordenar_nome_valor(self):

        response = self.client.get(self.url + '?ordering=nome,valor')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['nome'], 'Job')
        self.assertEqual(data[0]['valor'], '1800.00')
        self.assertEqual(data[-1]['nome'], 'Pagamento')
        self.assertEqual(data[-1]['valor'], '-100.00')

    def test_lista_ordenar_nomeDesc_valorAsc(self):

        response = self.client.get(self.url + '?ordering=-nome,valor')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['nome'], 'Pagamento')
        self.assertEqual(data[0]['valor'], '-200.00')
        self.assertEqual(data[-1]['nome'], 'Job')
        self.assertEqual(data[-1]['valor'], '2000.00')

    def test_lista_ordenar_nomeDesc_valorDesc(self):

        response = self.client.get(self.url + '?ordering=-nome,-valor')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['nome'], 'Pagamento')
        self.assertEqual(data[0]['valor'], '-100.00')
        self.assertEqual(data[-1]['nome'], 'Job')
        self.assertEqual(data[-1]['valor'], '1800.00')

    def test_lista_ordenar_valor_nome(self):

        response = self.client.get(self.url + '?ordering=valor,nome')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['nome'], 'Pagamento')
        self.assertEqual(data[0]['valor'], '-200.00')
        self.assertEqual(data[-1]['nome'], 'Job')
        self.assertEqual(data[-1]['valor'], '2000.00')

    def test_lista_ordenar_valorDesc_nomeAsc(self):

        response = self.client.get(self.url + '?ordering=-valor,nome')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['nome'], 'Job')
        self.assertEqual(data[0]['valor'], '2000.00')
        self.assertEqual(data[-1]['nome'], 'Pagamento')
        self.assertEqual(data[-1]['valor'], '-200.00')

    def test_lista_ordenar_valorDesc_nomeDesc(self):

        response = self.client.get(self.url + '?ordering=-valor,-nome')
        data = json.loads(json.dumps(response.data))
        self.assertEqual(data[0]['nome'], 'Job')
        self.assertEqual(data[0]['valor'], '2000.00')
        self.assertEqual(data[-1]['nome'], 'Pagamento')
        self.assertEqual(data[-1]['valor'], '-200.00')

