from django.shortcuts import render
from rest_framework import generics, filters
from .models import Niv
from .serializers import NivSerializer
from django_filters.rest_framework import DjangoFilterBackend


#import pdb
# Create your views here.

class NivsById(generics.ListAPIView):
	queryset = Niv.objects.all()
	serializer_class = NivSerializer
	filter_backends = (filters.SearchFilter,)
	search_fields = ('identification',)