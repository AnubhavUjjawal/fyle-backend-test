from django.shortcuts import render, get_object_or_404
from rest_framework import generics

from .errors import MissingQueryParameterException
from .models import Banks, Branches
from .serializers import BankSerializer, BranchSerializer


class BranchListView(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        bank_name = self.request.query_params.get('bank_name')
        city = self.request.query_params.get('city')
        if city is None and bank_name is None:
            raise MissingQueryParameterException(
                detail='city and bank_name missing in query params. Provide at least one.')
        results = None
        if city:
            res = Branches.objects.filter(city=city)
        if bank_name:
            res = res.filter(bank__name=bank_name)
        return res


class BranchRetrieveView(generics.RetrieveAPIView):
    serializer_class = BranchSerializer

    def get_object(self):
        ifsc = self.kwargs.get('ifsc', None)
        if ifsc is None:
            raise MissingQueryParameterException(
                detail='ifcs code missing in url params.')

        return get_object_or_404(Branches, ifsc=ifsc)
