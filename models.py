from django.db import models
import unittest
from UnitTest.DjangoUnitTest.views import index
# Create your models here.


class Service(models.Model):
    address = models.SlugField()
    ValueStaff = models.IntegerField()


class Staff(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=25)
    position = models.CharField(max_length=20)
    maritalStatus = models.CharField(max_length=10)
    education = models.CharField(max_length=30)
    age = models.IntegerField()


class Position(models.Model):
    NamePosition = models.CharField(max_length=35)


class Equipment(models.Model):
    instruments = models.CharField(max_length=50)


class Timetable(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    instruments = models.CharField(max_length=50)
    DateTime = models.DateTimeField(null=True)