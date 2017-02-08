from __future__ import unicode_literals

from django.db import models

# Create your models here.

class test(models.Model):
	username = models.EmailField(max_length=256)
	password = models.CharField(max_length=200)
	userid = models.SmallIntegerField(null=True)
	reqid = models.SmallIntegerField(default=0)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

class dev(models.Model):
	name = models.CharField(max_length=50)
	branch = models.CharField(max_length=50)
	sem = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	email = models.EmailField()
	linkedin = models.CharField(max_length=50)

class prof_contact(models.Model):
	name = models.CharField(max_length=50)
	desig = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	image = models.FileField(null=True)

class logo(models.Model):
	name = models.CharField(max_length=120)
	image = models.FileField(null=True)