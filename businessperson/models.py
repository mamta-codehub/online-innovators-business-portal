from django.db import models
from datetime import date
from django.contrib.auth.models import User
from innovators.models import *

class Inquiry(models.Model):
	name=models.CharField(max_length=30,default='')
	email=models.CharField(max_length=50,default='')
	subject=models.TextField(default='')
	message=models.TextField(default='')
	date=models.DateField(default=date.today)

	class Meta:
		db_table='inquiry'

class Feedback(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE, default='')
	rating=models.CharField(max_length=30,default='')
	comment=models.TextField()
	date=models.DateField(default=date.today)

	class Meta:
		db_table='feedback'

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	gender=models.CharField(max_length=50)
	contact=models.BigIntegerField()
	address=models.CharField(max_length=100)
	dob=models.DateField(default=date.today)
	role = models.CharField(max_length=30,default='')
	password = models.CharField(max_length=30,default='')

	class Meta:
		db_table = 'profile'


class Order(models.Model):
	profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
	idea    = models.ForeignKey(Idea,on_delete=models.CASCADE)
	date    = models.DateField(default=date.today)
	status  = models.CharField(max_length=100, default='completed')
	innovator = models.ForeignKey(User,on_delete=models.CASCADE)
	
	class Meta:
		db_table = 'order'
			
			


