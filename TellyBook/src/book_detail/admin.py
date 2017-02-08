from django.contrib import admin

# Register your models here.
from .models import book_detail,track,req

class bookdetailadmin(admin.ModelAdmin):
	list_display=["userid","reqid","bdate","eventname","eventroom","status","date","time","etime","condby","condbyname"]

# class leavedetailadmin(admin.ModelAdmin):
# 	list_display=["userid","reqid","sdate","edate","reason","desc"]


class trackadmin(admin.ModelAdmin):
	list_display=["userid","reqid","step1","step2","step3","step4","message"]

class reqadmin(admin.ModelAdmin):
	list_display=["proid","userid","reqid"]


admin.site.register(book_detail,bookdetailadmin)
# admin.site.register(leave_detail,leavedetailadmin)
admin.site.register(track,trackadmin)

admin.site.register(req,reqadmin)
