from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.SiteArticle)
admin.site.register(models.BlogArticle)
admin.site.register(models.ArticleComment)
admin.site.register(models.Event)
admin.site.register(models.EventComment)