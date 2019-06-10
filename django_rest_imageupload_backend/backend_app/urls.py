from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('imageupload_rest.urls')),
    url(r'^', include('imageupload_frontend.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

