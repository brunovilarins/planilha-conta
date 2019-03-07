# -*- coding: utf-8 -*-
from rest_framework import serializers

from contas.models import Conta


class ContaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conta
        fields = ('nome', 'valor')
