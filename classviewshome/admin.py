from django.contrib import admin
from .models import Article, Book, CustomUser,Team

admin.site.register(Article)
admin.site.register(Book)
admin.site.register(CustomUser)
admin.site.register(Team)
# Register your models here.
