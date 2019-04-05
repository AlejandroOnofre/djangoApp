import json
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from .models import Company

from .serializers import CompanySerializer
# Create your tests here.

class CompanyViewSetTestCase(APITestCase):
	url = 'http://127.0.0.1:8000/company/'

	def test_company_get(self):

		new_user = User.objects.create(username = "newuser", email = "new@user.com", password = "newpass")
		new_token = Token.objects.create(user=new_user)

		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + new_token.key)

		response = self.client.get(self.url)
		self.assertEqual(200, response.status_code)
		
