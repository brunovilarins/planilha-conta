# -*- coding: utf-8 -*-
from django.db import models


class Conta(models.Model):

    class Meta:
        app_label = u'contas'
        verbose_name = u'Conta'
        verbose_name_plural = u'Contas'

    nome = models.CharField(verbose_name='Nome do Registro', max_length=50)
    valor = models.DecimalField(verbose_name=u'Valor em R$', decimal_places=2, max_digits=10)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nome
