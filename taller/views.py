from django.shortcuts import render

from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import viewsets

from .models import Operation, PreCita
from .serializers import OperationSerializer, PreCitaSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class ListJobs(generics.ListAPIView):
	queryset = Operation.objects.all()
	serializer_class = OperationSerializer
	filter_backends = (DjangoFilterBackend,)
	filter_fields = ('niv__niv',)

class PreCitaView(generics.ListCreateAPIView):
	queryset = PreCita.objects.all()
	serializer_class = PreCitaSerializer

	"""def post(self, request, *args, **kwargs):
		a_precita = PreCita.objects.create(
			niv=request.data["niv"],
			created=request.data["created"],
			preferred_date=request.data["preferred_date"],
			preferred_time=request.data["preferred_time"],
			mileage=request.data["mileage"]
			)

		return Response(
			data=PreCitaSerializer(a_precita).data,
			status=status.HTTP_201_CREATED
			)"""
