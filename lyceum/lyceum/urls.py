from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('', include('users.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
    path('feedback/', include('feedback.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
        )
    urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
    ]
