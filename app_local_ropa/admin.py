from django.contrib import admin
from .models import Prenda, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color', 'categoria', 'precio', 'fecha_publicacion')
    search_fields = ('nombre', 'color')
    list_filter = ('categoria', 'color')
    ordering = ('-fecha_publicacion',)