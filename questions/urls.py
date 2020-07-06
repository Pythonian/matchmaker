from django.urls import path

from . import views

app_name = 'questions'

urlpatterns = [
    path('<id>/', views.single, name='question_single'),
    path('', views.home, name='question_home'),
]