from django.db import models

# Create your models here.

class Institute(models.Model):

    institute_username = models.Char(max_length = 200, default = '')
    institute_name = models.Char(max_length = 200, default = '')
    institute_details = models.Char(max_length = 200, default = '')

class Student(models.Model):

    