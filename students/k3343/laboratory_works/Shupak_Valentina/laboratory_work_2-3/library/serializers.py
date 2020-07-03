from rest_framework import serializers
from .models import Book, ReadingRoom, Reader, BookPlace, TakingBook


class ReadingRoomSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Читальный зал"""

    class Meta:
        model = ReadingRoom
        fields = "__all__"


class ReaderCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления/обновления Читателя"""

    class Meta:
        model = Reader
        fields = "__all__"


class BookPlaceSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Расположение Книги"""
    book = serializers.SlugRelatedField(slug_field="name", read_only=True)
    reading_room = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = BookPlace
        fields = "__all__"


class BookPlaceUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления Расположения Книги """

    class Meta:
        model = BookPlace
        fields = ['id', 'number']


class BookPlaceCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления Расположения Книги """

    class Meta:
        model = BookPlace
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Книга"""
    places = BookPlaceSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления/обновления Книги """

    class Meta:
        model = Book
        fields = ['id', 'section', 'cipher']


class BookCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления/обновления Книги """

    class Meta:
        model = Book
        fields = "__all__"


class TakingBookSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Взятие книги"""
    book = serializers.SlugRelatedField(slug_field="name", read_only=True)
    reader = serializers.SlugRelatedField(slug_field="fio", read_only=True)

    class Meta:
        model = TakingBook
        fields = "__all__"


class TakingBookCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления/обновления Взятия книги """

    class Meta:
        model = TakingBook
        fields = "__all__"


class ReaderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Читатель"""
    reading_room = serializers.SlugRelatedField(slug_field="name", read_only=True)
    books = TakingBookSerializer(many=True)
    class Meta:
        model = Reader
        fields = "__all__"
