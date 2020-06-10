from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quests/', include('quests.api.endpoints')),
    path('users/', include('users.api.endpoints')),
]
