from django.contrib import admin
from django.urls import path, include

# for image files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('home.urls')),
    path('', include('blog.urls')),
    # path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for images
