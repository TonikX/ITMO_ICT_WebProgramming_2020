from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('quests/', include('quests.api.endpoints')),
    path('admin/', admin.site.urls),
]
