
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url (r'^$','newsletter.views.home',name='home'),
    url (r'^contact$','newsletter.views.contact',name='contact'),
    url (r'^example$','newsletter.views.example',name='example'),
    url (r'^about$','newsletter.views.about',name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
