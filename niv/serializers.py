from rest_framework import serializers
from .models import Niv

class NivSerializer(serializers.ModelSerializer):

	class Meta:
		model = Niv
		fields = ("niv", "owner", "purchase_date", "last_job", "vin", 
			"brand", "model", "color", "year", "plate_number", "identification")

	def to_representation(self, instance):
		rep = super(NivSerializer, self).to_representation(instance)
		rep['model'] = instance.model.model
		return rep