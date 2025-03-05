from django.db import models

class uploadedFiles(models.Model):
    name = models.CharField(max_length=260)
    owner = models.CharField(max_length=50)
    created  =  models.DateTimeField("Date Created")
    updated = models.DateTimeField("Last Updated")
    path = models.CharField(max_length=500)
