from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('projects/', views.projects, name='projects'),
    path('webinvestors/', views.webinvestors, name='webinvestors'),
]
