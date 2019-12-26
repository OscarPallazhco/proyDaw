from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Genero)
admin.site.register(Usuario)
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Intercambio)
admin.site.register(Calificacion)