from __future__ import unicode_literals

from django.db import models

# Create your models here.
class check_rooms(models.Model):
	userid = models.SmallIntegerField(null=True)
	capacity = models.SmallIntegerField()
	date = models.CharField(null=True,max_length=8)
	stime = models.CharField(null=True,default='01:00',max_length=5)#default=datetime.now)
	etime = models.CharField(null=True,default='01:00',max_length=5)
	proom = models.CharField(max_length=120)
	floor = models.SmallIntegerField()

	



class rooms(models.Model):
	name = models.CharField(max_length=120)
	incharge = models.CharField(max_length=120)
	desig = models.CharField(max_length=120)
	avail = models.SmallIntegerField(default='1')
	depart = models.CharField(max_length=50, default=' ')
	capacity = models.SmallIntegerField()
	floor = models.SmallIntegerField()
	mike = models.SmallIntegerField(default='0')
	stage = models.SmallIntegerField(default='0')
	projector = models.SmallIntegerField(default='0')
	msp = models.SmallIntegerField()
	image = models.FileField(null=True)


class booked(models.Model):
	userid = models.SmallIntegerField(null=True)
	reqid = models.SmallIntegerField(null=True)
	eventname = models.CharField(max_length=50)
	eventroom = models.CharField(max_length=50)
	desc = models.CharField(max_length=250)
	date = models.CharField(null=True,max_length=8)
	stime = models.CharField(max_length=5)#null=True,default=datetime.now)
	etime = models.CharField(max_length=5)
	image = models.FileField(null=True)



class incharge(models.Model):
	userid = models.SmallIntegerField()
	department = models.CharField(max_length=50)
	incharge = models.CharField(max_length=120)
	profid = models.SmallIntegerField(null=True)
	

	# def __unicode__(self):
	# 	return str(self.datetimeobject) + " other string return info"


class check_rooms2(models.Model):
	userid = models.SmallIntegerField()
	capacity = models.SmallIntegerField()
	date = models.DateField()
	stime = models.TimeField(null=True,default='01:00')#default=datetime.now)
	etime = models.TimeField(null=True,default='01:00')
	proom = models.CharField(max_length=120)
	floor = models.SmallIntegerField()
	mike = models.SmallIntegerField()
	stage = models.SmallIntegerField()
	projector = models.SmallIntegerField() 


