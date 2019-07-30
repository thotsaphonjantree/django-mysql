from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Major, Student
 
admin.site.register(Major)
admin.site.register(Student)