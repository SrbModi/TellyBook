from django.contrib import admin

# Register your models here.

from .models import Post

class AdminCust(admin.ModelAdmin):
	list_display = ["title","updated","date","timestamp","content"]
admin.site.register(Post, AdminCust)