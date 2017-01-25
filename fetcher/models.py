from django.db import models

# Create your models here.

class Chart(models.Model):
    created = models.DateTimeField(auto_created=True)
    data = models.TextField()
    number1 = models.CharField(max_length=256)