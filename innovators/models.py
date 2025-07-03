from django.db import models
from myadmin.models import Category,Subcategory
from django.contrib.auth.models import User

class Idea(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE,default='')
	subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE,default='')
	title=models.CharField(max_length=200)
	smalldescription=models.TextField()
	largedescription=models.TextField()
	setupprice=models.CharField(max_length=50)
	setupduration=models.CharField(max_length=250)
	file_name=models.CharField(max_length=255,default='')
	file_name1=models.CharField(max_length=255,default='')
	user=models.ForeignKey(User,on_delete=models.CASCADE,default='')

	class Meta:
		db_table='idea'



