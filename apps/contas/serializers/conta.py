# -*- coding: utf-8 -*-
from rest_framework import serializers

from contas.models import Conta


class ContaSerializer(serializers.ModelSerializer):

    usuario = serializers.HiddenField(default=None)

    class Meta:
        model = Conta
        fields = ('nome', 'valor', 'usuario')
