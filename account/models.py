from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    
    def __str__(self):
        return str(self.username)