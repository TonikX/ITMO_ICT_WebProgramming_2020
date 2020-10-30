from django.contrib import admin

from lib_app.models import Hall, Book, Reader, Attachment


class HallAdmin(admin.ModelAdmin):

    list_display = ("name", "capacity")


class BookAdmin(admin.ModelAdmin):

    list_display = ("title", "author", "publisher", "edition_year",
                    "sphere", "cipher", "receipt_date", "hall")


class ReaderAdmin(admin.ModelAdmin):

    list_display = ("library_card_num", "full_name", "passport_data",
                    "birth_date", "home_address", "phone_num",
                    "education", "degree", "hall"
                    )


class AttachmentAdmin(admin.ModelAdmin):

    list_display = ("reader", "book", "attachment_starting_date",
                  "attachment_finishing_date")

admin.site.register(Hall, HallAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Attachment, AttachmentAdmin)
