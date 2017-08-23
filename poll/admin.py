from django.contrib import admin

from .models import Category, Contestant, Vote, Sum

# Register your models here.

admin.site.register(Category)
admin.site.register(Contestant)
admin.site.register(Vote)
admin.site.register(Sum)
