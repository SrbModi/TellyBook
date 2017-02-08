from django.contrib import admin

# Register your models here.

from .models import check_rooms,rooms, incharge,booked

class checkroomadmin(admin.ModelAdmin):
	list_display = ["capacity","floor","date","stime","etime"]

class roomsadmin(admin.ModelAdmin):
	list_display=["name","depart","incharge","desig","image","capacity","floor","mike","stage","projector"]

class bookedadmin(admin.ModelAdmin):
 	list_display=["userid","reqid","eventname","eventroom","desc","date","stime","etime"]

class inchargeadmin(admin.ModelAdmin):
	list_display=["userid","department","incharge","profid"]

admin.site.register(check_rooms,checkroomadmin)
admin.site.register(rooms,roomsadmin)
admin.site.register(booked,bookedadmin)
admin.site.register(incharge,inchargeadmin)