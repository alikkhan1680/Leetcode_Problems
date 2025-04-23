from django.contrib import admin

# Register your models here.
from django.contrib import admin

from app.models import *
class UsersAdmin(admin.ModelAdmin):
    admin.site.register(Product)
    admin.site.register(Student)
    admin.site.register(User)