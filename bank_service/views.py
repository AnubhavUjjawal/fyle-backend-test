from django.shortcuts import render, get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.decorators import action

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

    city_param = openapi.Parameter(
        'city',
        openapi.IN_QUERY,
        description="The city to query for.",
        type=openapi.TYPE_STRING)
    bank_name_param = openapi.Parameter(
        'bank',
        openapi.IN_QUERY,
        description="The bank name to search for.",
        type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[
        city_param, bank_name_param
    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BranchRetrieveView(generics.RetrieveAPIView):
    serializer_class = BranchSerializer

    def get_object(self):
        ifsc = self.kwargs.get('ifsc', None)
        if ifsc is None:
            raise MissingQueryParameterException(
                detail='ifcs code missing in url params.')

        return get_object_or_404(Branches, ifsc=ifsc)
