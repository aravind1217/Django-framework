from django.db import models

class Friend(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	mobile_no = models.CharField(max_length=100)
	email = models.EmailField()
	location = models.CharField(max_length= 100)
	dob = models.DateField(auto_now= False, auto_now_add= False)

	def __str__(self):
		return f'{self.first_name+ " " + self.last_name}'




