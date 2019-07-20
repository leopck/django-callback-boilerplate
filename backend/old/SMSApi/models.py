from django.db import models

class Distribution(models.Model):
    version = models.CharField(max_length=255)
    create = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.EmailField()