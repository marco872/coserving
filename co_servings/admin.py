from django.contrib import admin

# Register your models here.
from .models import Webinvestor, Project, Liquidity_Pool, Investment, Development, Venue, Liquidity, Building, Plan, Token, Guest

admin.site.register(Webinvestor)
admin.site.register(Project)
admin.site.register(Liquidity_Pool)
admin.site.register(Investment)
admin.site.register(Development)
admin.site.register(Venue)
admin.site.register(Liquidity)
admin.site.register(Building)
admin.site.register(Plan)
admin.site.register(Token)
admin.site.register(Guest)


