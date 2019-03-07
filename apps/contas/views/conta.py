# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, ListAPIView

from contas.models import Conta
from contas.serializers.conta import ContaSerializer


class ContaAPIView(ListAPIView):
    serializer_class = ContaSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Conta.objects.filter(usuario=request.user)
        return self.list(request, *args, **kwargs)
