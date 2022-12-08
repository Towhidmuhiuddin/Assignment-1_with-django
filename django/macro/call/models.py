from django.db import models
from django.urls import reverse 

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    city = models.CharField(max_length=50)
    rating = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('home')

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    trainer = models.CharField(max_length=100, default="Rahima")    
    student_numbers = models.IntegerField(default =0)    
    weekly_class = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.trainer} - {self.student_numbers} - {self.weekly_class}"

    def get_absolute_url(self):
        return reverse ('home')

class Teacher(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subject = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=20)     

    def __str__(self):
        return f"{self.name} - {self.subject} - {self.email}" 

    def get_absolute_url(self):
        return reverse ('home')      

