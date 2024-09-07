from django.db import models


class Hello(models.Model):
	name = models.CharField(max_length=20)
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
