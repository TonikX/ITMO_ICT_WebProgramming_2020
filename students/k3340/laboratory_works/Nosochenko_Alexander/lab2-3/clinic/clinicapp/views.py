from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *


class DoctorListView(APIView):
    permission_classes = [permissions.AllowAny]
    "Вывод списка докторов"
    def get(self, request):
        doctor = Doctor.objects.all()
        serializer = DoctorsSerializer(doctor, many=True)
        return Response(serializer.data)

    def post(self, request):
        doctor = DoctorsSerializer(data=request.data)
        if doctor.is_valid():
            doctor.save()
        return Response(status=201)


class DoctorEditView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        serializer = DoctorsSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        doctor = Doctor.objects.get(pk=pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class ClientsListView(APIView):
    "Вывод списка транзакций"
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        clients = Patient.objects.all()
        serializer = ClientsSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        client = ClientsSerializer(data=request.data)
        if client.is_valid():
            client.save()
        return Response(status=201)


class ClientsEditView(APIView):
    "Изменение списка транзакций"
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk, format=None):
        client = Patient.objects.get(pk=pk)
        serializer = ClientsSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        transactions = Patient.objects.get(pk=pk)
        transactions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecordsListView(APIView):
    permission_classes = [permissions.AllowAny]
    "Вывод списка докторов"
    def get(self, request):
        record = Medicalrecord.objects.all()
        serializer = MedicalrecordSerializer(record, many=True)
        return Response(serializer.data)

    def post(self, request):
        record = MedicalrecordCreateSerializer(data=request.data)
        if record.is_valid():
            record.save()
        return Response(status=201)


class RecordsEditView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        record = Medicalrecord.objects.get(pk=pk)
        serializer = MedicalrecordCreateSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        record = Medicalrecord.objects.get(pk=pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CabinetListView(APIView):
    permission_classes = [permissions.AllowAny]
    "Вывод списка докторов"
    def get(self, request):
        cabinet = Cabinet.objects.all()
        serializer = CabinetSerializer(cabinet, many=True)
        return Response(serializer.data)

    def post(self, request):
        cabinet = CabinetCreateSerializer(data=request.data)
        if cabinet.is_valid():
            cabinet.save()
        return Response(status=201)


class CabinetEditView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        cabinet = Cabinet.objects.get(pk=pk)
        serializer = CabinetCreateSerializer(cabinet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cabinet = Cabinet.objects.get(pk=pk)
        cabinet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionListView(APIView):
    "Вывод списка транзакций"
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        transaction = Transactions.objects.all()
        serializer = TransactionListSerializer(transaction, many=True)
        return Response(serializer.data)

    def post(self, request):
        transaction = TransactionCreateSerializer(data=request.data)
        if transaction.is_valid():
            transaction.save()
        return Response(status=201)


class TransactionEditView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        transaction = Transactions.objects.get(pk=pk)
        serializer = TransactionCreateSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = Transactions.objects.get(pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReceptionListView(APIView):
    "Вывод списка транзакций"
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        reception = Reception.objects.all()
        serializer = ReceptionSerializer(reception, many=True)
        return Response(serializer.data)

    def post(self, request):
        transaction = ReceptionCreateSerializer(data=request.data)
        if transaction.is_valid():
            transaction.save()
        return Response(status=201)


class ReceptionEditView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        reception = Reception.objects.get(pk=pk)
        serializer = ReceptionCreateSerializer(reception, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reception = Reception.objects.get(pk=pk)
        reception.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewsListView(APIView):
    "Вывод списка транзакций"
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        reviews = Reviews.objects.all()
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        reviews = ReviewsCreateSerializer(data=request.data)
        if reviews.is_valid():
            reviews.save()
        return Response(status=201)


class ReviewsEditView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, pk):
        reviews = Reviews.objects.get(pk=pk)
        serializer = ReviewsCreateSerializer(reviews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        reviews = Reviews.objects.get(pk=pk)
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)