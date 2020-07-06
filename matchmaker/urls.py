from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', dashboard.views.home, name='home'),
    path('question/<id>/', 'questions.views.single', name='question_single'),
    path('question/', 'questions.views.home', name='question_home'),
    path('contact/', 'newsletter.views.contact', name='contact'),
    path('about/', 'matchmaker.views.about', name='about'),
    path('like/<id>/', 'likes.views.like_user', name='like_user'),
    path('profile/edit/', 'profiles.views.profile_edit', name='profile_edit'),
    path('profile/<username>/',
        'profiles.views.profile_view', name='profile'),
    path('profile/jobs/add/', 'profiles.views.job_add', name='job_add'),
    path('profile/jobs/edit/', 'profiles.views.jobs_edit', name='jobs_edit'),

    path('profile/', 'profiles.views.profile_user', name='profile_user'),

    path('admin/', include(admin.site.urls)),
    path('accounts/', include('registration.backends.default.urls')),
    path('matches/', include('matches.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
