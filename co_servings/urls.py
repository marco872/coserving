from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('liquiditypools/', views.liquiditypools),

    path('projects/', views.projects),
    path('webinvestors/', views.webinvestors),
]
