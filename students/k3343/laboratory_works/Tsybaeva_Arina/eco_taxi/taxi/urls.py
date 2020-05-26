from django.urls import path
from . import views

driver_detail = views.DriverViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

storage_detail = views.OrderViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}
)
urlpatterns=[
    path('drivers/', views.DriverListView.as_view()),
    path('driver/<int:pk>/', driver_detail),
    path('order/', views.OrderCreateView.as_view()),
    path('client/', views.YoungListView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    path('order-list/', views.DriverOrderView.as_view()),
    path('week/', views.WeekDayOrderView.as_view()),
    path('top/', views.TopCategoryView.as_view()),
    path('storage_client/', views.StorageClientView.as_view()),
    path('new-driver/', views.DriverCreateView.as_view()),
    path('delete-driver/<int:pk>/', views.DriverDeleteView.as_view()),
    path('storage/', views.StorageView.as_view()),
    path('report/', views.ToFabricTrashView.as_view()),
    path('add_order/', views.OrderStorageCreateView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('delete-order/<int:pk>', storage_detail),
    path('total_storage/', views.TotalStorageView.as_view()),
    path('add_client/', views.ClientView.as_view()),
    path('logout/', views.Logout.as_view())

]

