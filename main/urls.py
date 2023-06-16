from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('comment_form/', views.comment_form, name='comment_form'),
    path('get_comments/', views.get_comments, name='get_posts'),
    path('animals/', views.animals),
    path('finder/', views.finder),
    path('care/', views.care),
    path('authorization/',  views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
    path('account/', views.account, name='account'),
    path('account/', views.update_account, name='update_account'),
]
