from rest_framework import serializers
from ..models import interests

class CreateInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = interests
        fields = ('__all__')