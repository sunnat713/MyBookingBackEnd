from django.shortcuts import render
from rest_framework.generics import *

from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HomeApiView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = HomeSerializer

