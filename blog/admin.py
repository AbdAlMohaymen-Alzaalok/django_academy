from django.contrib import admin
from . import models

@admin.register(models.Blog)
class AdminBlog(admin.ModelAdmin):
    list_per_page = 3