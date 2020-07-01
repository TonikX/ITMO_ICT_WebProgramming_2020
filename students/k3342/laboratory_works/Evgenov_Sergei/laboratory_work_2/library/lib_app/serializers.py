from rest_framework import serializers
from lib_app.models import Hall, Book, Reader, Attachment


class HallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = ("name", "capacity")


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("title", "author", "publisher", "edition_year",
                  "sphere", "cipher", "receipt_date", "hall")


class ReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = ("id", "library_card_num", "full_name", "passport_data",
                  "birth_date", "home_address", "phone_num",
                  "education", "degree", "hall"#, "books"
                  )


class ReaderSerializer_2(serializers.ModelSerializer):

    class Meta:
        model = Reader
        fields = ("id", "library_card_num", "full_name")


class BookSerializer_2(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("title", "author", "cipher", "hall")


class BookSerializer_3(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("cipher", "hall")


class AttachmentSerializer(serializers.ModelSerializer):

    reader = ReaderSerializer_2()
    book = BookSerializer_2()
    class Meta:
        model = Attachment
        fields = ("id", "reader", "book", "attachment_starting_date",
                  "attachment_finishing_date")


class AttachmentSerializer_2(serializers.ModelSerializer):

    book = BookSerializer_2()
    class Meta:
        model = Attachment
        fields = ("book", "attachment_starting_date")


class AttachmentSerializer_3(serializers.ModelSerializer):

    # book = BookSerializer_3()
    class Meta:
        model = Attachment
        fields = ("reader", "book", "attachment_starting_date")
