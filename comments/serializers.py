from .models import Comments
from rest_framework import serializers

from general.serializers import UserSerializer

class CommentsSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Comments
		fields = ('id', 'user', 'title', 'comment')
	  