from rest_framework import serializers
from .models import IhaFeatures

class IhaFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = IhaFeatures
        fields = '__all__'