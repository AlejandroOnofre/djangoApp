from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

	title = models.CharField(max_length=250)
	comment = models.TextField()