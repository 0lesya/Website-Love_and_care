from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('animals/', views.animals),
    path('finder/', views.finder),
    path('care/', views.care),
    path('authorization/', views.login),
]
