from rest_framework import serializers
from .models import Operation, PreCita, Cita
from niv.models import Niv

class OperationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Operation
		fields = ("niv", "job", "date", "description")

	def to_representation(self, instance):
		rep = super(OperationSerializer, self).to_representation(instance)
		rep['niv'] = instance.niv.niv
		return rep

class PreCitaSerializer(serializers.ModelSerializer):
	niv = serializers.CharField()

	class Meta:
		model = PreCita
		fields = ("niv", "created", "preferred_date", "preferred_time", "mileage")

	def create(self, validated_data):
		niv = validated_data.pop('niv')
		niv_instance, created = Niv.objects.get_or_create(niv=niv)
		precita_instance = PreCita.objects.create(**validated_data, niv=niv_instance)
		return precita_instance