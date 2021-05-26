from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.wall),
    path('logout', views.logout),
    path('messages', views.message),
    path('comments/<int:message_id>', views.comment),
]