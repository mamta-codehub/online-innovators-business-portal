from django.db import models

class Category(models.Model):
	categoryname=models.CharField(max_length=30,default='')
	
	def __str__(self):
		return self.categoryname

	class Meta:
		db_table='category'

class Subcategory(models.Model):
	subcategoryname=models.CharField(max_length=30)
	category=models.ForeignKey(Category,on_delete=models.CASCADE,default='')
	file_name=models.CharField(max_length=255,default='')

	def __str__(self):
		return self.subcategoryname

	class Meta:
		db_table='subcategory'

	



