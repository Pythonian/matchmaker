from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', include('dashboard.urls')),
    path('question/', include('questions.urls')),
    # path('contact/', 'newsletter.views.contact', name='contact'),
    path('like/', include('likes.urls')),
    path('profile/', include('profiles.urls')),

    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('matches/', include('matches.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
