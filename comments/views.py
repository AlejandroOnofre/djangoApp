from django.shortcuts import render
from .models import Comments
from rest_framework import viewsets
from comments.serializers import CommentsSerializer 


# Create your views here.
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer