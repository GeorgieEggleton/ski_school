from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('lessons/', include('lessons.urls')),
    path('bag/', include('bag.urls')),
    path('payment/', include('payment.urls')),
    path('profiles/', include('profiles.urls')),
    path('marketing/', include('marketing.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

