from django.contrib import admin
from .models import Grupo, Integrante, Proyecto, Tarea

admin.site.register(Grupo)
admin.site.register(Integrante)
admin.site.register(Proyecto)
admin.site.register(Tarea)