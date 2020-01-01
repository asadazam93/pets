from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateField()

    class Meta:
        abstract = True


class Dog(Animal):
    owner = models.ForeignKey(User, related_name='dogs', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cat(Animal):
    owner = models.ForeignKey(User, related_name='cats', on_delete=models.CASCADE)

    def __str__(self):
        return self.name