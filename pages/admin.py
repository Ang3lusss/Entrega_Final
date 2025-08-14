from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha_publicacion', 'autor')
    search_fields = ('titulo', 'bajada', 'cuerpo')
    list_filter = ('fecha_publicacion', 'autor')
