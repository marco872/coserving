from django.contrib import admin

# Register your models here.
from .models import Webinvestor, Project, Liquidity_Pool, Investment, Development, Venue


admin.site.register(Webinvestor)
admin.site.register(Project)
admin.site.register(Liquidity_Pool)
admin.site.register(Investment)
admin.site.register(Development)
admin.site.register(Venue)