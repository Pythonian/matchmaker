from django.urls import path

from . import views

urlpatterns = [
    path('<id>/', views.like_user, name='like_user'),
]