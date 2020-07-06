from django.urls import path

from . import views

urlpatterns = [
    path('<id>/', views.single, name='question_single'),
    path('', views.home, name='question_home'),
]