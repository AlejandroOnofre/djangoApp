from django.shortcuts import render
from .models import Company
from rest_framework import viewsets
from company.serializers import CompanySerializer 
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer