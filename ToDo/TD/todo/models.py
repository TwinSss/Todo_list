from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	text = models.CharField(max_length=40)
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.text
		
class Client(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name