from django.contrib import admin
from .models import Post
from .models import Libro

# Register your models here.


admin.site.register(Post)


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editorial', 'ano', 'nivel')
    search_fields = ('titulo', 'autor')
    fields = ('titulo', 'autor', 'editorial', 'ano', 'nivel', 'enlace', 'resumen', 'imagen')  # Agregar imagen