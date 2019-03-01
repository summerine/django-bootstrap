from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=150)
	address = models.TextField(blank=True, null=False)
	dob = models.DateField(blank=True, null=True, verbose_name="DOB")
	phone = models.CharField(max_length=30, blank=True)
