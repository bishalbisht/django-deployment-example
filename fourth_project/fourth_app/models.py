from django.db import models

# Create your models here.

class User(models.Model):
    full_name= models.CharField(max_length=260)
    first_name= models.CharField(max_length=160)
    last_name = models.CharField(max_length=160)
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.full_name)