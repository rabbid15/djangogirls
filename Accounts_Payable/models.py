from django.db import models

class account(models.Model):
	company = models.CharField(max_length=10)
	paydate = models.IntegerField()


# Create your models here.
