from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from company.models import Company

# Create your models here.
#class Profile(models.Model):
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	#company = models.OneToOneField(Company, on_delete=models.CASCADE)



#@receiver(post_save, sender= User)
#def create_or_update_user(sender, instance, created, **kwargs):
	#if created:
		#Profile.objects.create(user=instance)

	#instance.profile.save()