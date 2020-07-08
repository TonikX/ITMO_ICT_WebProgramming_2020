from django.contrib import admin
from .models import Company, Direction, Gate, Flight, Comments, CommentCategory

admin.site.register(Company)

admin.site.register(Direction)

admin.site.register(Gate)

admin.site.register(Flight)

admin.site.register(CommentCategory)

admin.site.register(Comments)


