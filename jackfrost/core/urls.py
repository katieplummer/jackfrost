from django.urls import path, include
from django.contrib import admin
from jackfrost.apps.blog.views import index_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
    path('blog/', include("jackfrost.apps.blog.urls")),
    path('shop/', include("jackfrost.apps.shop.urls")),
    path('info/', include("jackfrost.apps.info.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)