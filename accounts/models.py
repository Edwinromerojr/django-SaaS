from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=255)
    max_num_links = models.IntegerField()

    def __str__(self):
        return self.name


class User(AbstractUser):
    plan = models.ForeignKey(Plan, related_name='users', default=1, on_delete=models.CASCADE)
    pass
