from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Experience, BlogPost

admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(BlogPost)