from django.contrib import admin

# Register your models here.

from .models import test,dev,prof_contact,logo

class testmodeladmin(admin.ModelAdmin):
	list_display = ["username","password","userid","reqid","timestamp","updated"]

class devadmin(admin.ModelAdmin):
	list_display=["name","branch","sem","phone","email","linkedin"]

class logoadmin(admin.ModelAdmin):
	list_display=["name","image"]

class prof_contactadmin(admin.ModelAdmin):
	list_display=["name","desig","phone","image"]

admin.site.register(test,testmodeladmin)
admin.site.register(dev,devadmin)
admin.site.register(logo,logoadmin)
admin.site.register(prof_contact,prof_contactadmin)