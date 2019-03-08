from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import auth

# Create your models here.

class Faculty(models.Model):
    username = models.IntegerField()
    password = models.TextField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField(name="Date of Birth")

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def create(self):
        new_user = User.objects.create_user(username=self.username, password=self.password)

        Students = Group.objects.get(name='Students')
        Students.user_set.add(new_user)

        new_user.first_name = self.first_name
        new_user.last_name = self.last_name
        new_user.save()
