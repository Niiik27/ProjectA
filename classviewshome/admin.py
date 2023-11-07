from django.contrib import admin
from .models import Article, Book, CustomUser

admin.site.register(Article)
admin.site.register(Book)
admin.site.register(CustomUser)
# Register your models here.
