from django.contrib import admin
from .models import Articles,Category,Tag

from django.db import models
from markdownx.widgets import AdminMarkdownxWidget
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    list_display=("title","author","img","abstract","visited","created_at")
    search_fields=("title","author","abstract","visited","created_at")
    list_filter=list_display



admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Category,)
admin.site.register(Tag,)
