from django.contrib import admin

# Register your models here.
from .models import Webinvestor, Project

admin.site.register(Webinvestor)
admin.site.register(Project)
