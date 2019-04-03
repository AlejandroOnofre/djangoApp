from .models import Company
from rest_framework import serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'phone_number', 'address')