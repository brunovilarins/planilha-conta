# -*- coding: utf-8 -*-
from django.core.exceptions import FieldError
from rest_framework.generics import ListCreateAPIView, ListAPIView

from contas.models import Conta
from contas.serializers.conta import ContaSerializer


class ContaAPIView(ListAPIView):
    serializer_class = ContaSerializer

    def get_queryset(self):
        ordering = self.request.query_params.get('ordering', None)
        contas = Conta.objects.filter(usuario=self.request.user)

        if ordering:
            order = ''
            for i in ordering.split(','):
                if i.replace('-','').replace(' ','') in Conta.__doc__:
                    if order:
                        order += ','
                    order += i.replace(' ','')
            if order:
                contas = contas.order_by(*order.split(','))

        return contas



