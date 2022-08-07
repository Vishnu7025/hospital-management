from typing_extensions import Self
from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name = models.CharField(max_length=155)
    dep_desc = models.TextField()

    def __str__(self):
        return self.dep_name
   