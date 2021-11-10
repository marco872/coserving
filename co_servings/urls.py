

from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name="home"),
    path('how/', views.how, name="how"),
    path('white/', views.white, name="white"),
    path('projects/', views.projects, name="projects"),
    path('liquiditypools/', views.liquiditypools, name="liquiditypools"),
    path('development/', views.development, name="development"),
    path('rental/', views.rental, name="rental"),
    path('venue/', views.venue, name="venue"),
  	path('liquidity/', views.liquidity, name="liquidity"),
  	path('buildings/', views.buildings, name="buildings"),
    path('plan/', views.plan, name="plan"),
    path('stand/', views.stand, name="stand"),
    path('token/', views.token, name="token"),
    path('guest/', views.guest, name="guest"),
    
]
