from django.db import models

# Create your models here.

class ToolConfiguration(models.Model):
    toolName = models.CharField(max_length=150)
    endPoint = models.URLField()
    authenticationType = models.CharField(max_length=100)
    userName = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    projectName = models.CharField(max_length=200, default='')

class Tools(models.Model):
    toolName = models.CharField(max_length=150)

class Projects(models.Model):
    projectName = models.CharField(max_length=200)

