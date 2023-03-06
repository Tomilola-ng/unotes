from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static  import static
from notes.views import *

urlpatterns = [
    path('auth/', admin.site.urls),

    path('ng/', home, name='homeView'),
    path('', RedirectView.as_view(url='ng/')),

    path('me/', me, name='meView'),

    path('notes/', include('notes.urls')),

    path('ckeditor/',include('ckeditor_uploader.urls')),

    path('register/', register, name='registerView'),

    path('account', include('django.contrib.auth.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)