from django.contrib.auth.models import User
from django.test import TestCase

from contas.models import Conta


class ContaTest(TestCase):
    """ Teste para o Model Conta """

    def setUp(self):
        Conta.objects.create(
            nome='Job', valor=1000.99, usuario=User.objects.first())
        Conta.objects.create(
            nome='Pagamento', valor=-128.9, usuario=User.objects.first())

    def test_conta(self):
        conta_job = Conta.objects.get(nome='Job')
        conta_pagamento = Conta.objects.get(nome='Pagamento')
        self.assertEqual(
            conta_job.nome, "Job")
        self.assertEqual(
            conta_pagamento.nome, "Pagamento")
