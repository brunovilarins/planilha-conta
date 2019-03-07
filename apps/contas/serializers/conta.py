# -*- coding: utf-8 -*-
from rest_framework import serializers

from contas.models import Conta


class ContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conta
        fields = ('nome', 'valor')


class FormContaSerializer(serializers.Serializer):

    usuario = serializers.HiddenField(default=None)
    tipo = serializers.ChoiceField(choices=('Entrada', 'Saída'))
    nome = serializers.CharField(max_length=50)
    valor = serializers.DecimalField(max_digits=10, decimal_places=2)
