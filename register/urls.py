from django.urls import path, include
from django.conf.urls.static import static
from register.views import Register
from django.conf import settings

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name = 'register')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)