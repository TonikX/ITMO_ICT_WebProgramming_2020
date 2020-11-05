from django.contrib import admin

from .models import Visitor
admin.site.register(Visitor)
from .models import Book
admin.site.register(Book)
from .models import Hall
admin.site.register(Hall)
from .models import Librarian
admin.site.register(Librarian)
from .models import Ownership
admin.site.register(Ownership)
from .models import Accessory
admin.site.register(Accessory)
from .models import Rent
admin.site.register(Rent)
