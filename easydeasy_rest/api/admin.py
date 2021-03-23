from django.contrib import admin
from .models import Article, Disease, Site, Category, Feed, DefaultCategoryImage

admin.site.register(Site)
admin.site.register(Disease)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Feed)
admin.site.register(DefaultCategoryImage)
