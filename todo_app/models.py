from django.db import models 

class TODO(models.Model):
    Title=models.CharField(max_length=200)
    status=models.CharField(max_length=200)