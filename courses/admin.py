from django.contrib import admin
from . import models

@admin.register(models.Course)
class AdminCourse(admin.ModelAdmin):
    list_per_page = 3
