from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from lib_app.models import Hall, Book, Reader, Attachment
from lib_app.serializers import HallSerializer, BookSerializer, ReaderSerializer
from lib_app.serializers import AttachmentSerializer, AttachmentSerializer_2
from lib_app.serializers import AttachmentSerializer_3, AttachmentSerializer_4
from lib_app.serializers import BookSerializer_4


class Hall_V(APIView):

    def get(self, request):
        halls = Hall.objects.all()
        serializer = HallSerializer(halls, many=True)
        return Response(serializer.data)


class Book_V(APIView):

    def get(self, request):
        book = request.GET.get("book")
        books = Book.objects.filter(cipher=book)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class Books_V(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer_4(books, many=True)
        return Response(serializer.data)


class Reader_V(APIView):

    def get(self, request):
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response(serializer.data)

    def post(self, request):
        readers =  ReaderSerializer(data=request.data)
        if readers.is_valid():
            readers.save()
            return Response({"status": 201})
        else:
            return Response({"status": 400})


class Attachment_V(APIView):

    def get(self, request):
        attachments = Attachment.objects.all()
        serializer = AttachmentSerializer(attachments, many=True)
        return Response({"data": serializer.data})


class Reader_books(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        person = request.GET.get("reader")
        reader_full = Reader.objects.filter(id=person)
        reader = ReaderSerializer(reader_full, many=True)
        attachments = Attachment.objects.filter(reader=person, attachment_finishing_date=None)
        serializer = AttachmentSerializer_2(attachments, many=True)
        return Response({"reader": reader.data,"books": serializer.data})

    def post(self, request):
        attachments =  AttachmentSerializer_3(data=request.data)
        if attachments.is_valid():
            attachments.save()
            return Response({"status": 201})
        else:
            return Response({"status": 400})


class Detach(viewsets.ModelViewSet):

    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer_4
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class Reader_change(viewsets.ModelViewSet):

    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class Reader_del(APIView):

    permission_classes = [permissions.IsAuthenticated, ]

    def delete(self, request, pk):
        reader = Reader.objects.get(pk=pk)
        reader.delete()
        return Response({"status": "Delete"})


class Book_add(APIView):

    def post(self, request):
        book =  BookSerializer_4(data=request.data)
        if book.is_valid():
            book.save()
            return Response({"status": 201})
        else:
            return Response({"status": 400})


class Book_one(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer_4(books, many=True)
        return Response(serializer.data)
