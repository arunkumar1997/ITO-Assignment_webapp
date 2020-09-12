from django.db import models

# Create your models here.
class Car(models.Model):
	Company = models.CharField(max_length=100)
	Model = models.CharField(max_length=100)
	Color =models.CharField(max_length=100)
	Date = models.CharField(max_length=100)
	Price = models.CharField(max_length=100)
	Engine_capacity = models.CharField(max_length=100)
	Number_plate = models.CharField(max_length=100)
	Seating_capacity = models.CharField(max_length=10)

def __str__(self):
	return self.Company