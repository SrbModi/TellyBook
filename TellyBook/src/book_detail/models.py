from __future__ import unicode_literals

from django.db import models

# Create your models here.

class book_detail(models.Model):
	userid = models.SmallIntegerField()
	reqid = models.SmallIntegerField(default = '10')
	eventname = models.CharField(max_length=120)
	eventroom = models.CharField(max_length=120)
	bdate = models.DateField(auto_now_add=True,null=True) #change the date-time format
	date = models.CharField(null=True, max_length=10)
	time = models.TimeField(null=True)
	etime = models.TimeField(null=True)
	status = models.SmallIntegerField(default=0)
	condby = models.CharField(max_length=25)
	condbyname = models.CharField(max_length=50)
	desc = models.TextField()


# class leave_detail(models.Model):
# 	userid=models.SmallIntegerField()
# 	reqid=models.SmallIntegerField()
# 	sdate = models.DateField()
# 	edate = models.DateField()
# 	reason = models.TextField(max_length=120)
# 	desc = models.TextField()


class track(models.Model):
	userid = models.SmallIntegerField(default = '0')
	reqid = models.SmallIntegerField(default = '0')
	message = models.CharField(max_length=200, default=' ')
	step1 = models.SmallIntegerField(default=0)
	step2 = models.SmallIntegerField(default=-2)
	step3 = models.SmallIntegerField(default=-2)
	step4 = models.SmallIntegerField(default=-2)
	n=models.SmallIntegerField(default=1)

class req(models.Model):
	proid=models.SmallIntegerField()
	userid=models.SmallIntegerField()
	reqid=models.SmallIntegerField()