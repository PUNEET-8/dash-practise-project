from django.db import models

# Create your models here.
class Interview(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveIntegerField()

