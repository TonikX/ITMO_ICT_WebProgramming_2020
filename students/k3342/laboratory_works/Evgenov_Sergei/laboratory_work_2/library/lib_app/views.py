from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from lib_app.models import Hall, Book, Reader, Attachment
from lib_app.serializers import HallSerializer, BookSerializer, ReaderSerializer
from lib_app.serializers import AttachmentSerializer, AttachmentSerializer_2


class Hall_V(APIView):

    def get(self, request):
        halls = Hall.objects.all()
        serializer = HallSerializer(halls, many=True)
        return Response(serializer.data)


class Book_V(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class Reader_V(APIView):

    def get(self, request):
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response(serializer.data)


class Attachment_V(APIView):

    def get(self, request):
        attachments = Attachment.objects.all()
        serializer = AttachmentSerializer(attachments, many=True)
        return Response({"data": serializer.data})


class Books_person(APIView):

    def get(self, request):
        person = request.GET.get("reader")
        reader_full = Reader.objects.filter(id=person)
        reader = ReaderSerializer(reader_full, many=True)
        attachments = Attachment.objects.filter(reader=person, attachment_finishing_date=None)
        serializer = AttachmentSerializer_2(attachments, many=True)
        return Response({"reader": reader.data,"books": serializer.data})
