from django.contrib import admin

from .models import Author, Quote, Tag


admin.site.register(Tag)
admin.site.register(Quote)
admin.site.register(Author)