from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=25)
    designation=models.CharField(max_length=120)
    salary=models.IntegerField()
    location=models.CharField(max_length=120)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name
