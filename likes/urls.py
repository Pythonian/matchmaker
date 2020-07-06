from django.urls import path

from . import views

app_name = 'likes'

urlpatterns = [
    path('<id>/', views.like_user, name='like_user'),
]