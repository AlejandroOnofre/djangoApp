from django.contrib.auth.models import User
from rest_framework import serializers

from company.models import Company
#from .models import Profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
	    model = User
	    fields = ('url', 'username', 'email', 'is_staff')


#class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	#company = serializers.StringRelatedField(many=True)

	#class Meta:
		#model = Profile
		#fields = ('company')
