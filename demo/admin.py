from django.contrib import admin

# Register your models here.

from demo.models import Project, Blog

admin.site.register(Project)

admin.site.register(Blog)