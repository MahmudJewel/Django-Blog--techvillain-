from django.contrib import admin
from blog import models

# Register your models here.

admin.site.register(models.category)
admin.site.register(models.subCategory)
admin.site.register(models.blogPost)
