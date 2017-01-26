from django.db import models

# Create your models here.

class Chart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    data = models.TextField(blank=True, null=True)
    number1 = models.CharField(max_length=256, blank=True, null=True)