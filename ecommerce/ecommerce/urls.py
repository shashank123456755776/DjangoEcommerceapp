from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # ✅ Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ecommerceapp.urls")),
    path('auth/', include("authcart.urls")),
]

# Serve media files only in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
