from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import redirect_hw

urlpatterns = [
    path('', redirect_hw),
    path('admin/', admin.site.urls),
    path('hw/', include('hw.urls')),
    path('accounts/', include('allauth.urls'))
]
