import datetime
from django.db.models import Count, Sum
from .models import Driver, Order, Client, Storage, Category
from .serializers import (DriverDetailSerializer, DriverListSerializer, OrderCreateSerializer,
                          OrderDetailSerializer, YoungClientSerializer, DriverOrderSerializer,
                          WeekOrderSerializer, TopCategorySerializer, StorageSerializer,
                          TotalTrashSerializer, StorageCreateOrderSerializer, ClientSerializer, CategorySerializer)
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ClientFilter, OrderFilter
from rest_framework import viewsets, filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class DriverListView(generics.ListAPIView):
    """Вывод списка водителей"""
    queryset = Driver.objects.all()
    serializer_class = DriverListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DriverDetailView(generics.RetrieveAPIView):
    """Вывод водителя"""
    queryset = Driver.objects.all()
    serializer_class = DriverDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderCreateView(generics.CreateAPIView):
    """Добавление нового заказа"""
    serializer_class = OrderCreateSerializer
    #permission_classes = [permissions.IsAuthenticated]


class OrderListView(generics.ListAPIView):
    """Вывод заказов"""
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    #permission_classes = [permissions.IsAdminUser]


class YoungListView(generics.ListAPIView):
    """Вывод списка клиентов моложе 40"""
    queryset = Client.objects.all()
    serializer_class = YoungClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = ClientFilter
    filter_backends = (DjangoFilterBackend,)


class Client1View(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DriverOrderView(generics.ListAPIView):
    """Заказы определенного водителя за указанную дату"""
    queryset = Order.objects.all()
    serializer_class = DriverOrderSerializer
    #permission_classes = [permissions.IsAdminUser]
    filter_backends = (filters.SearchFilter, )
    search_fields = ('data', 'driver__name')


class WeekDayOrderView(generics.ListAPIView):
    """Количество заказов в процентном отношении за каждый день недели"""
    def get_queryset(self):
        total_amount = Order.objects.count()
        order = Order.objects.values('data__week_day').annotate(percent=Count('id')*(100/total_amount)).order_by('data__week_day')
        return order
    serializer_class = WeekOrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopCategoryView(generics.ListAPIView):
    """Топ 3 часто сдаваемых категории"""
    def get_queryset(self):
        order = Order.objects.values('category__name').annotate(amount=Count('id')).order_by('-amount')[:3]
        return order
    serializer_class = TopCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StorageClientView(generics.ListAPIView):
    """Объем мусора, забранный у клиентов"""
    def get_queryset(self):
        trash = Storage.objects.values('order__category').annotate(amount=Sum('order__mass'))
        return trash
    serializer_class = TopCategorySerializer
    #permission_classes = [permissions.IsAdminUser]


class StorageView(generics.ListAPIView):
    """Объем мусора на складе"""
    def get_queryset(self):
        trash = Storage.objects.values('order__category').annotate(amount=Sum('order__mass')).order_by('-amount')
        return trash
    serializer_class = StorageSerializer
    permission_classes = [permissions.IsAdminUser]


class ToFabricTrashView(generics.ListAPIView):
    """Отчет за месяц"""

    def get_queryset(self):
        today = datetime.date.today()
        trash_client = Order.objects.filter(data__month=today.month).aggregate(total=Sum('mass'))
        trash_storage = Storage.objects.filter(order__data__month=today.month).aggregate(total=Sum('order__mass'))
        total_client = Order.objects.filter(data__month=today.month).count()
        total_money = Order.objects.filter(data__month=today.month).aggregate(money=Sum('cost'))
        passed = trash_client['total'] - trash_storage['total']
        trash = [{"total_to_fabric": passed, "total_from_client": trash_client['total'], "total_client": total_client, "total_money" :total_money['money']}]
        return trash
    serializer_class = TotalTrashSerializer
    permission_classes = [permissions.IsAdminUser]


class DriverCreateView(generics.CreateAPIView):
    """Добавление водителя"""
    serializer_class = DriverDetailSerializer
    permission_classes = [permissions.IsAdminUser]


class DriverDeleteView(generics.DestroyAPIView):
    """Удаление водителя"""
    queryset = Driver.objects.all()
    serializer_class = DriverDetailSerializer
    permission_classes = [permissions.IsAdminUser]


class OrderStorageCreateView(generics.CreateAPIView):
    """Добавление заказа на склад"""
    serializer_class = StorageCreateOrderSerializer
    permission_classes = [permissions.IsAdminUser]


class TotalStorageView(generics.ListAPIView):
    """Заказы, присутствующие на складе"""
    queryset = Storage.objects.all().order_by('order_id')
    serializer_class = StorageCreateOrderSerializer
    permission_classes = [permissions.IsAdminUser]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverDetailSerializer
    permission_classes = [permissions.IsAdminUser]


class OrderViewset(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateOrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientView(generics.CreateAPIView):
    serializer_class = ClientSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
