

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('how/', views.how, name="how"),
    path('projects/', views.projects, name="projects"),
    path('liquiditypools/', views.liquiditypools, name="liquiditypools"),
    path('development/', views.development, name="development"),
]