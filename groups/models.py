from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=40)
    visible = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    admins = models.ManyToManyField(User)
    
    def __str__(self):
        return self.name
    
