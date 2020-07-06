from django.urls import path

from . import views

urlpatterns = [
    path('position/<slug:slug>/',
         views.position_match_view,
         name='position_match_view_url'),
    path('employer/<slug:slug>/',
         views.employer_match_view,
         name='employer_match_view_url'),
    path('location/<slug:slug>/',
         views.location_match_view,
         name='location_match_view_url'),
]
