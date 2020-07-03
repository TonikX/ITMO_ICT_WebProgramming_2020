from django.urls import path
from . import views

urlpatterns = [
    path("resident/",views.ResidentViewSet.as_view({'get': 'list'})),
    path("resident/<int:pk>/",views.ResidentViewSet.as_view({'get': 'retrieve'})),
    path("resident/create",views.ResidentViewSet.as_view({'post': 'create'})),
    path("resident/<int:pk>/delete",views.ResidentViewSet.as_view({'delete': 'destroy'})),
    path("resident/<int:pk>/update",views.ResidentViewSet.as_view({'post': 'update'})),
    path("servant/", views.ServantViewSet.as_view({'get': 'list'})),
    path("servant/<int:pk>/",views.ServantViewSet.as_view({'get': 'retrieve'})),
    path("servant/create",views.ServantViewSet.as_view({'post': 'create'})),
    path("servant/<int:pk>/update",views.ServantViewSet.as_view({'post': 'update'})),
    path("servant/<int:pk>/delete",views.ServantViewSet.as_view({'delete': 'destroy'})),
    path("cleaning/", views.CleaningViewSet.as_view({'get': 'list'})),
    path("cleaning/<int:pk>/",views.CleaningViewSet.as_view({'get': 'retrieve'})),
    path("cleaning/create",views.CleaningViewSet.as_view({'post': 'create'})),
    path("cleaning/<int:pk>/update",views.CleaningViewSet.as_view({'post': 'update'})),
    path("cleaning/<int:pk>/delete",views.CleaningViewSet.as_view({'delete': 'destroy'})),
    path("floor/", views.FloorViewSet.as_view({'get': 'list'})),
    path("floor/<int:pk>/", views.FloorViewSet.as_view({'get': 'retrieve'})),
    path("roomtype/", views.RoomTypeViewSet.as_view({'get': 'list'})),
    path("roomtype/<int:pk>/", views.RoomTypeViewSet.as_view({'get': 'retrieve'})),
    path("room/", views.RoomViewSet.as_view({'get': 'list'})),
    path("room/<int:pk>/", views.RoomViewSet.as_view({'get': 'retrieve'})),
]