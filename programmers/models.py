from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Programmer(models.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    language = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.user.get_full_name()

class Project(models.Models):
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
