# -*- coding: utf-8 -*-
from decimal import Decimal

from django.core.exceptions import FieldError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from contas.models import Conta
from contas.serializers.conta import ContaSerializer, FormContaSerializer


class ContaAPIView(ListAPIView):
    serializer_class = ContaSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

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


class FormContaAPIView(CreateAPIView):
    serializer_class = FormContaSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        conta = Conta()
        conta.usuario = request.user
        conta.nome = serializer.data['nome']
        conta.valor = Decimal(serializer.data['valor'])
        if serializer.data['tipo'] == 'Saída':
            conta.valor = conta.valor * -1
        conta.save()
        serializer.data['valor'] = conta.valor
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

