from django.contrib import admin

from .models import App

# Register your models here.

class AppAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",'phone')

admin.site.register(App, AppAdmin)