from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	SapID = models.IntegerField(default=60000000000)

	def __str__(self):
		return self.user.username


