from django.contrib import admin
from .models import Articles
# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    list_display=("title","author","img","abstract","visited","created_at")
    search_fields=("title","author","abstract","visited","created_at")
    list_filter=list_display



admin.site.register(Articles,ArticlesAdmin)