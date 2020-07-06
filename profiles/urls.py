from django.urls import path

from . import views

urlpatterns = [
    path('edit/', views.profile_edit, name='profile_edit'),
    path('<username>/', views.profile_view, name='profile'),
    path('jobs/add/', views.job_add, name='job_add'),
    path('jobs/edit/', views.jobs_edit, name='jobs_edit'),
    path('', views.profile_user, name='profile_user'),
]