from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('<programmer_id>/', views.index , name = 'index')
]
