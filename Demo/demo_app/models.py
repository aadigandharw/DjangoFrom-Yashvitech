from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=50)
    user_class = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TimeField()
