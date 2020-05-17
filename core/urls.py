from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'core'



urlpatterns = [
    path('', views.home, name='home'),
    path('gate/<int:no>/entry/', views.StationEntryView, name='gate_entry'),
    path('gate/<int:no>/exit/', views.StationExitView, name='gate_exit'),
]
