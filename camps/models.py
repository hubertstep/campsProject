from django.db import models

class Pupils(models.Model):
    name = models.CharField(max_length=200)
