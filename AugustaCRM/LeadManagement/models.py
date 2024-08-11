import datetime
from django.db import models

# Create your models here.
class NewLeads(models.Model):
    currenttimemillis = models.CharField(max_length= 50, primary_key=True)
    name = models.CharField(max_length= 100, null = True)
    email = models.CharField(max_length= 50, null = True)
    phone = models.CharField(max_length = 50, null =True)
    platform = models.CharField(max_length = 100, null = True)
    timestamp = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=20)
    attempt = models.IntegerField(default= 0)


class CallList(models.Model):
    currenttimemillis = models.CharField(max_length= 50, primary_key=True)
    name = models.CharField(max_length= 100, null = True)
    email = models.CharField(max_length= 50, null = True)
    phone = models.CharField(max_length = 50, null =True)
    platform = models.CharField(max_length = 100, null = True)
    timestamp = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=20)
    attempt = models.IntegerField(default= 0)


class ArchiveLeads(models.Model):
    currenttimemillis = models.CharField(max_length= 50, primary_key=True)
    name = models.CharField(max_length= 100, null = True)
    email = models.CharField(max_length= 50, null = True)
    phone = models.CharField(max_length = 50, null =True)
    platform = models.CharField(max_length = 100, null = True)
    timestamp = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=20)
    attempt = models.IntegerField(default= 0)