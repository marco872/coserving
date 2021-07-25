from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('liquiditypools/', views.liquiditypools, name='liquiditypools'),

    path('projects/', views.projects, name='projects'),
    path('webinvestors/', views.webinvestors, name='webinvestors'),
]
