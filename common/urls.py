"""mvtblog URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage

from blog.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
	path('account/', include('account.urls')),
	path('blog/', include('blog.urls')),
	path('link/', include('link.urls')),
    # ThirdParty
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
