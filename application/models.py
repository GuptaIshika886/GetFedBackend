from django.db import models

class RegisteredUsers(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    pwd=models.CharField(max_length=100)
    cpwd=models.CharField(max_length=100)

class RegisteredCntnOwners(models.Model):
    username=models.CharField(max_length=100)
    cname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    pwd=models.CharField(max_length=100)
    cpwd=models.CharField(max_length=100)

class Canteen(models.Model):
    c_id=models.CharField(max_length=12)
    c_email=models.EmailField(max_length=100)
    c_name=models.CharField(max_length=100)
    c_address=models.CharField(max_length=100)
    c_phoneNo=models.CharField(max_length=10)
    c_feedback=models.IntegerField()

class Categories(models.Model):
    c_id=models.CharField(max_length=12)
    item_name=models.CharField(max_length=100)
    item_price=models.FloatField(max_length=5)

class ViewProfile(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)