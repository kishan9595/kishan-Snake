from django.contrib import admin
from .models import Article, Review

class ArticleAdmin(admin.ModelAdmin):
    list_dispaly = ['title']
    serach_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Review)