from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)