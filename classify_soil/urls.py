from django.urls import path
from classify_soil import views

urlpatterns = [
    path('', views.index, name='index')
]
