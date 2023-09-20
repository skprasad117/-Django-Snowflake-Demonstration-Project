from django.db import models

class SnowflakeData(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()