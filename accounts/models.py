from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Employee(AbstractUser):
    department = models.CharField(max_length=255, null=True, blank=True)
